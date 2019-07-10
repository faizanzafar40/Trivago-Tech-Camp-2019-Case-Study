import get_links
import get_images
import get_word_freq
import sys
import os
import linecache
import datetime
import re
import requests
import urllib3
import time
from bs4 import BeautifulSoup
import json
from PIL import Image
import cv2
import numpy as np
import errno
from lxml import html  
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup, NavigableString, Tag
import nltk
import nltk.data
from collections import Counter

path = 'extracted_pictures'


if __name__ == "__main__":

    i = 1
    
    urls = ["http://localhost/test/Ada_Lovelace.html", "http://localhost/test/Alan_Turing.html", "http://localhost/test/Blaise_Pascal.html", "http://localhost/test/Donal_Knuth.html", "http://localhost/test/Grace_Hopper.html", "http://localhost/test/Konrad_Zuse.html", "http://localhost/test/Richard_Stallman.html"]

    while(i!=0):
        
        print("<<<A SIMPLE APP FOR EXTRACTING INFORMATION FROM HTML PAGES>>> \n")
        print("Option 1. Extract all links \n")
        print("Option 2. Extract all images and get information about their attributes \n")
        print("Option 3. Extract all text and know the frequency of different word categories \n")
        print("Option 0. Exit the App \n")
        
        user_input = int(input("Type your menu option number and press Enter: "))

        if(user_input == 1):
            
            links = []
            for url in urls:
                
                print("Links from URL: ", url)
                a = get_links.get_links(url, links)
                
                for i in a:
                    print(i)
                    print("\n")
                
                get_links.save_to_json(a)
            
            continue

        elif(user_input == 2):
            
            for url in urls:
                get_images.download_images(url)
            
            for filename in os.listdir(path):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".svg"):
                    
                    try:
                        os.chdir(path)
                        a = os.path.join('./', filename)
                        image_path = a
                        image = Image.open(a)           
                        get_images.extract_image_attributes(image_path, image)
                        os.chdir('..')
                        raise IOError
                    
                    except IOError:
                        print("Sorry, the image file at", path,a, "seems to be corrupted :(")    
                    continue
                
                else:
                    continue

            continue

        elif(user_input == 3):
        
            for url in urls:
                
                print("Text from URL: ", url)
                url_text = get_word_freq.get_text(url)
                print(url_text)
                
                print("Word Categories from URL: ", url)
                tokens = nltk.word_tokenize(url_text)
                url_text_tags = nltk.pos_tag(tokens)
                dict_url_text_tags = dict(url_text_tags)
                
                for key, val in sorted(dict_url_text_tags.items()):
                    print(key + ":", val)
                
                count_var = Counter(tag for word,tag in url_text_tags)
                
                for word in sorted(count_var):
                    print(word + ":", count_var[word])

            continue

        elif(user_input == 0):

            print("See you next time!")
            quit()

    i=i+1