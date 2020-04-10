# Moon Phase Animation

This program downloads 8761 pictures of moon going through every phase and liberation of moon for 2019 and makes a smooth animation in form of a .gif file. The pictures are downloaded from  NASA website listed [here](https://svs.gsfc.nasa.gov/4442).


## Getting Started

### prerequisites
This programs uses imageio module which can be downloaded from pip.
```
pip install imageio
```
or by running the requirements.txt to get the version used while making this program.
```
pip install -r requirements.txt
```

### Usage
```
python moon.py
```
Some useful arguments
```
-h, --help            show this help message and exit
-f FREQUENCY, --frequency FREQUENCY
                       frequency of download
-srt START, --start START
                       start position
-stp STOP, --stop STOP
                       stop position
```
As the complete set of pictures is very large, these arguments are useful in creating smaller gifs. For example, to make a gif of first 500 images with every 5th image, try:
```
python moon.py -srt 1 -stp 500 -f 5
```

## Result
This is a gif of first 50 images:

![Image](phases.gif)

The data can go well over 300Mb and take a long time to download and the gif itself will be over 100Mb.

## Notes
  * Usege of moon_det.py is same as moon.py
  * Each image downloaded by moon_det.py is over 10Mb so it'll take a really, really long time to download pictures for a good gif :(
