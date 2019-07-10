from PIL import Image
import os
import cv2
import numpy as np
import errno
import requests  
from lxml import html  
import sys  
import urllib3
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def download_images(url):
    
    response = requests.get(url)
    
    html_parse = html.fromstring(response.text)

    images = html_parse.xpath('//img/@src')  
    if not images:  
        sys.exit("Found No Images")

    images = [urljoin(response.url, url) for url in images]  
    print ('Found %s images' % len(images))

    for url in images[0:10]:
        # This range can be adjusted to limit the number of extracted images
        response = requests.get(url)
        folder = open('extracted_pictures/%s' % url.split('/')[-1], 'wb')
        
        # Pictures will be downloaded to directory 'extracted_pictures'
        folder.write(response.content)
        folder.close()

def extract_image_attributes(image_path, image_obj):

    image_format = image_obj.format
    image_color_mode = image_obj.mode
    image_size = image_obj.size

    print("Attributes of image: %s" % image_path)
    print("The file format of the image is: %s" % image_format)
    print("The mode of the image is: %s" % image_color_mode)
    print("The size of the image is: width %d pixels, height %d pixels" % image_size)