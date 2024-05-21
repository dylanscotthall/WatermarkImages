# WatermarkImages
This python script watermark all images in a folder or folder of folders with the images parent folders name

## How to use
First get the .exe onto your machine either by selecting the .exe and then selecting download raw at the top right or by cloning the whole repository by using 
git clone https://github.com/dylanscotthall/WatermarkImages

BEFORE YOU RUN THE SCRIPT MAKE A COPY OF ALL YOUR IMAGES THIS PROCESS IS NOT REVERSABLE

once the .exe is on your machine you can run it from the console.
navigate to the directory where you downloaded your .exe and right click in the directory and select 'Open in Terminal'
Once you have a terminal open type addTextToImage.exe followed by the path to you folder containing all the images you want to rename
The script takes in three parameter 

-- font which you need to specify a .ttf font or you can use the default one provided in the repository when you use git clone

-- scale which defaults to 0.05 if you do not specify it, this is the size of the text relative to each image

-- position which defaults to bottom_right the other option are top_left, top_right and bottom_left

for this script to run your folder structure for the images must look like this

```bash
└───Root
    ├───Folder 1
    │       imag1.png
    │       image2.png
    │       image3.png
    │
    ├───Folder 2
    │       imag1.png
    │       image2.png
    │       image3.png
    │
    └───Folder 3
            imag1.png
            image2.png
            image3.png
```
With this folder structure you can run the script like this
addTextToImage.exe /path/to/root --scale 0.05 --font Roboto-Black.ttf --position bottom_right
