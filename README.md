# TangkaForSIRR

# Introduction
This is the Thangka dataset for SIRR that listed in paper "Single Image Reflection Removal with Reflection Classifier and Gradient Restorer." . Any research work on this data set should place proper citation of this paper.

# How to read the json files?

We provide a simple Python program called "imgORjson.py" for converting .jpg and .json in the file, the image and the label information can be directly read from the .json file.

Users can also read JSON files through applications such as LabelMe.

# Files in the project
There are 2 directories, "400_origin" and "2000_split".
400_origin---contains 0-399 files, the corresponding image is an unprocessed original image
2000_split---contains 0-1999 files, the corresponding image is the image obtained by clipping the original image, and all image sizes are 256 * 256