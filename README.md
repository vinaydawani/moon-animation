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

## Result
This is a gif of first 50 images:

![Image](phases.gif)

The data can go well over 300Mb and take a long time to download and the gif itself will be over 100Mb.

## Updates in Progress
1. Implementing a step feature that will allow to download every n<sup>th</sup> image rathher than all 8761 images which will save time. Although the animationwill be not as smooth.
2. Another script that will download more detailed and higher quality pictures with position angle and liberation of moon.
