import os
import argparse
from urllib import request as req
from imageio import imread, mimsave


parser = argparse.ArgumentParser(description="Taking some flags")
parser.add_argument('-f', '--frequency', default=1,
                    help='frequency of download')
parser.add_argument('-srt', '--start', default=1, help='start position')
parser.add_argument('-stp', '--stop', default=8760, help='stop position')
args = parser.parse_args()


def get_image(img_num, directory):
    url = 'https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/5760x3240_16x9_30p/fancy/comp.{}.tif'.format(img_num)
    img_name = directory + img_num + '.tif'
    req.urlretrieve(url, img_name)
    return


def add_zeroes(img_num):
    return '{:04d}'.format(img_num)


def make_gif(start_num, end_num, directory, freq):
    #  files = [img for img in os.listdir(directory) if '.jpg' in img]

    images = []
    for img_num in range(start_num, end_num, freq):
        img_name = directory + add_zeroes(img_num) + '.tif'
        images.append(imread(img_name))

    mimsave('detailed_phases.gif', images)

    return


def main(start_num=1, end_num=8760, freq=1):
    directory = 'images2/'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, img_num in enumerate(range(start_num, end_num + 1, freq)):
        percent = round(img_num / (end_num / 100))
        img_num = add_zeroes(img_num)

        if os.path.exists(directory + img_num + '.tif'):
            print(
                f"Image {img_num + '.tif'} already available in\
                 directory {directory}")
            continue

        while True:
            try:
                get_image(img_num, directory)

                bar = (
                    "|"
                    + "█" * int(0.5 * percent)
                    + "-" * int(0.5 * (100 - percent))
                    + "|"
                )

                print('\033c')

                status = "Downloaded {}/{}, {}% ".format(
                    i + 1, end_num//freq, percent)
                print("Collecting images")
                print('  ' + status)
                print('     ' + bar)

            except Exception as e:
                print(e)
                continue
            break

    make_gif(start_num, end_num, directory, freq)
    return


if __name__ == '__main__':
    main(int(args.start), int(args.stop), int(args.frequency))
