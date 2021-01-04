from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
PATH = "/Users/samaylakhani/Documents/chromedriver"
# driver = webdriver.Chrome(PATH)
# driver.maximize_window()


with open('UKR.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# Navigate to url with video being appended to search_query
# driver.get('https://www.youtube.com/results?search_query={}'.format(str(video))