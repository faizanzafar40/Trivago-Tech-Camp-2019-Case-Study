import sys
import os
import linecache
import datetime
import re
import requests
import urllib3
import time
from bs4 import BeautifulSoup


if __name__ == "__main__":


    def getLinks(url):
        html_page = urllib3.PoolManager()
        response = html_page.request('GET', url)
        soup = BeautifulSoup(response.data.decode('utf-8'), "html.parser")
        links = []

        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            links.append(link.get('href'))

        return links

    print(getLinks("https://faizanzafar40.github.io/"))