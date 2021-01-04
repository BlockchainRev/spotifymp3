from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe', chrome_options=opt)
driver.get("http://youtube.com")
driver.find_element_by_name("search_query").send_keys("Python")
driver.find_element_by_id("search-icon-legacy").click()
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
links = driver.find_elements_by_id("video-title")
PATH = "/Users/samaylakhani/Documents/chromedriver"

def open_video(link_to_vid):
    formatted_link = link_to_vid.replace(' ', '+')
    driver.get('https://www.youtube.com/results?search_query={}'.format(str(formatted_link)))

def iterate_over_list(csv_to_list_of_songs):
    for item in csv_to_list_of_songs:
        open_video(item)

