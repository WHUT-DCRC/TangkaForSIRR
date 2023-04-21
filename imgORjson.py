import base64
import json
import os
import cv2
from sys import argv
from base64 import b64encode
from json import dumps

# set 'utf-8'
ENCODING = 'utf-8'

array_of_img = [] # this if for store all of the image data
# this function is for read image,the input is directory name
def img2json(imgdir,jsondir):
    for filename in os.listdir(r"./"+imgdir):
        #print(filename) #just for test

        #read image data from imgdir
        IMAGE_NAME = imgdir + "/" + filename
        JSON_NAME = (jsondir + "/" + filename).replace('jpg','json')
        print(IMAGE_NAME,JSON_NAME)

        # read img
        with open(IMAGE_NAME, 'rb') as jpg_file:
            byte_content = jpg_file.read()

        # img to base64
        base64_bytes = b64encode(byte_content)

        # base64 to utf-8
        base64_string = base64_bytes.decode(ENCODING)

        # save
        raw_data = {}
        raw_data["name"] = IMAGE_NAME
        raw_data["image_base64_string"] = base64_string

        #  to json , "  "split
        json_data = dumps(raw_data, indent=2)

        # save json to jsondir
        with open(JSON_NAME, 'w') as json_file:
            json_file.write(json_data)


def json2img(jsondir,imgdir):
    for filename in os.listdir(r"./"+jsondir):
        #print(filename) #just for test
        #img is used to store the image data
        JSON_NAME = jsondir + "/" + filename
        IMAGE_NAME = (imgdir + "/" + filename).replace('json','jpg')

        # read json file
        with open(JSON_NAME, "r") as json_file:
            raw_data = json.load(json_file)
        # get base64 str
        image_base64_string = raw_data["image_base64_string"]
        # base64 to img
        image_data = base64.b64decode(image_base64_string)
        # save image
        with open(IMAGE_NAME, 'wb') as jpg_file:
            jpg_file.write(image_data)


if __name__ == "__main__":
    imgdir = "2000img"
    jsondir = "2000_split"
    img2json(imgdir,jsondir)

    # use test dir
    # imgdir = "2000img_test"
    # jsondir = "2000json_test"

    # json2img(jsondir,imgdir)


