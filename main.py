from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
PATH = "/Users/samaylakhani/Documents/chromedriver"
import urllib.request
from bs4 import BeautifulSoup
import os
import youtube_dl
import csv
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(PATH, chrome_options=options)
wait = WebDriverWait(driver, 10)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
youtube_links = []
search_list = []
# --------------------------------------------------------------------------------------------------- 
def open_and_save_link(link_to_vid):
    # formatted_link = link_to_vid.replace(' ', '+')
    driver.get('https://www.youtube.com/')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(link_to_vid)
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    youtube_links.append(WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))[0].get_attribute("href"))

def iterate_over_list(csv_to_list_of_songs):
    for item in csv_to_list_of_songs:
        open_and_save_link(item)

def generate_search(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for item in data:
        search_list.append(item[0]+' '+item[1])
    search_list.pop(0)
 
def links_to_txt():
    with open('links.txt', 'w') as f:
        for item in youtube_links:
           f.write("%s\n" % item)

def download_function():
    # os.chdir('Your Music')
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192'
        }]
    }
    with open('links.txt') as f:
        urls = f.readlines()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def main():
    filename = input('What is the name of the .csv [name.csv]? :')
    generate_search(filename)
    iterate_over_list(search_list)
    links_to_txt()
    print("File written to links.txt")
    download_function()
    print('done')

main()