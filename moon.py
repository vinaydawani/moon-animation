from urllib import request as req
import os
from imageio import imread, mimsave


def get_image(img_num, directory):
    url = 'https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/730x730_1x1_30p/moon.{}.jpg'.format(img_num)
    img_name = directory + img_num + '.jpg'
    req.urlretrieve(url, img_name)
    return

def add_zeroes(img_num):
    return '{:04d}'.format(img_num)

def make_vid(start_num, end_num, directory):
    files = [img for img in os.listdir(directory) if '.jpg' in img]

    images = []
    for img_num in range(start_num, end_num):
        img_name = directory + add_zeroes(img_num) + '.jpg'
        images.append(imread(img_name))

    mimsave('phases.gif', images)

    return

def main(start_num = 1, end_num = 8761):
    directory = 'images/'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, img_num in enumerate(range(start_num, end_num+1)):
        percent = round(img_num/(end_num/100))
        img_num = add_zeroes(img_num)

        if os.path.exists(directory + img_num + '.jpg'):
            print(f"Image {img_num + '.jpg'} already available in directory {directory}")
            continue

        while True:
            try:
                get_image(img_num, directory)

                bar = (
                        "["
                        + "#" * int(0.5 * percent)
                        + "-" * int(0.5* (100 - percent))
                        + "]"
                )

                print('\033c')

                status = "Downloaded {}/{}, {}% ".format(i+1, end_num, percent)
                print(status + bar)

            except Exception as e:
                print(e)
                continue
            break

    make_vid(start_num, end_num, directory)
    return

if __name__ == '__main__':
    start = int(input("start: "))
    stop = int(input("Stop: "))
    main(start, stop)
