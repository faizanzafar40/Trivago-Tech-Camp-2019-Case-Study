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
import csv

def get_links(url, links):
    
    html_render = urllib3.PoolManager()
    html_response = html_render.request('GET', url)
    soup = BeautifulSoup(html_response.data.decode('utf-8'), "html.parser")

    a_tags = soup.findAll('a')
    for link in a_tags:
        links.append(link.get('href'))

    return links

def save_to_json(links):

            for link in links:
                with open('links.json', 'a+') as output_file:
                    json.dump(link, output_file)
                    output_file.write('\n')