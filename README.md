## Haze-Removal-Using-Dark-Channel-Prior-and-Guided-Filter
* This project is mainly based on the work of [**Kaiming He**](http://kaiminghe.com/) who is my favorite researcher.<br>
---
#### Contents

1. [Environments](#Environments)
1. [Packages](#Packages)
1. [Methods](#Methods)
1. [Usage](#Usage)
1. [Results](#Results)
1. [References](#references)
---

#### Environments

###### &emsp;Python&ensp;3.0.0 or newer<br>
* I do suggest you use python 3 which is both stable and widely used nowadays.
* The code also works well with python 2 since I just use numpy and matplotlib.

#### Packages

###### &emsp;numpy<br>
###### &emsp;matplotlib<br>
* The requirement to the version of these packages is not strict, because we just use the basic function.  
* The tools used to read image is matplotlib which is in the order of RGB while cv2 is in the order of BGR.
* I want to remind you that even the same operator can have different meanings between matrix and array in numpy.

#### Methods

* ###### &ensp;[Dark Channel Prior---CVPR 2009](http://kaiminghe.com/publications/cvpr09.pdf)<br>
&emsp; This method was mainly put forward by [**Kaiming He**](http://kaiminghe.com/), and then it was published at CVPR 2009 which was rated as the best paper.<br>
* ###### &ensp;[Guided Image Filtering---ECCV 2010](http://kaiminghe.com/publications/eccv10guidedfilter.pdf)<br>
&emsp; This method help us get a fine haze removal image in a fast way with less cost compared with matting method.<br>
* ###### &ensp;[Matting Laplacian Matrix---CVPR 2006](https://ieeexplore.ieee.org/document/4359322)<br>
&emsp; From [paper](http://kaiminghe.com/publications/cvpr09.pdf), we can see that the matting laplacian is the inspiration of guided image filter, they are both ingenious and attractive.

#### Usage
 * I don't want to package the code so that you can see the details, and you are welcomed to give me suggestion.
 * The variables used in my code are as same as these in official papers so that you can get it easily.
 * The function `haze_removal()` contains each step used in image de-hazing, I wrote this just for convenience. 

#### Results

* [**Tiananmen Square**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/plane.jpg)&ensp;:&ensp;the original image comes from Kaiming He's paper<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_tiananmen.png /><br><br>

* [**The Forbidden City**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/palace.jpg)&ensp;:&ensp;the original image comes from Kaiming He's paper<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_dark_channel.png /><br><br>

* [**New York**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/plane.jpg)&ensp;:&ensp;the original image comes from Kaiming He's paper<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_ny.png /><br><br>

* [**HongKong**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/plane.jpg)&ensp;:&ensp;the original image comes from Kaiming He's paper<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_hk.png /><br><br> 

* [**Airport**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/plane.jpg)&ensp;:&ensp;the original image is downloaded from internet<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_plane.png /><br><br> 

* [**The Street**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/street.jpg)&ensp;:&ensp;the original image is downloaded from internet<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_street.png /><br><br>

* [**A380 is taking off**](https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/image/a380.jpg)&ensp;:&ensp;the original image is downloaded from internet<br>
<img src= https://github.com/ForeverPs/haze-removal-using-dark-channel-prior-and-guided-filter/blob/master/results/haze_removal_a380.png /><br><br>

#### References

##### Author&ensp;:&ensp;Kaiming He, Jian Sun, Xiaoou Tang<br>
* ###### &ensp;[Single Image Haze Removal Using Dark Channel Prior----CVPR 2009](http://kaiminghe.com/publications/cvpr09.pdf)<br>
* ###### &ensp;[Guided Image Filtering----ECCV 2010](http://kaiminghe.com/publications/eccv10guidedfilter.pdf)<br><br>

##### Author&ensp;:&ensp;Anat Levin, Dani Lischinski, Yair Weiss<br>
* ###### &ensp;[A Closed Form Solution to Natural Image Matting----CVPR 2006](https://ieeexplore.ieee.org/document/4359322)<br><br>

