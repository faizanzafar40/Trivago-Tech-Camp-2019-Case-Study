import urllib3
from bs4 import BeautifulSoup, NavigableString, Tag
import json
import nltk
import nltk.data
from collections import Counter

def get_text(url):
    
    html_render = urllib3.PoolManager()
    html_response = html_render.request('GET', url)
    soup = BeautifulSoup(html_response.data.decode('utf-8'), "html.parser")
    
    for script in soup(["script", "style"]):
        script.extract()

    all_text = soup.get_text()

    whites = (line.strip() for line in all_text.splitlines())
    chunks = (phrase.strip() for line in whites for phrase in line.split("  "))
    all_text = '\n'.join(chunk for chunk in chunks if chunk)

    return all_text