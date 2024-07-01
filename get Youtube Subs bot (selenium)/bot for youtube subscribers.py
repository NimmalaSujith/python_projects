from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import os

delay_action = 6  # delay for action
delay_popup = 40  # delay for get stats

chrome_location_path = "C:\script folder\chromedriver.exe"
driver = webdriver.Chrome(chrome_location_path)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# --------login to gmail account ---------
email = "sujithsubs03@gmail.com"
password_in = "Sujit"
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element(By.ID,"identifierId").send_keys(email)
driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
time.sleep(3)
pa = driver.find_element(By.NAME,"password").send_keys(password_in)
driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
time.sleep(5)
#------------------subpals code-------------------
subpals_password="sujith"
driver.get("https://www.subpals.com/login/final/UCcFrrU5HatzM6JNuQAjw-Ew/")
driver.find_element(By.XPATH,'//*[@id="core-wrapper"]/section/div/div/div/div/div/form/div[2]/input').send_keys(subpals_password)
driver.find_element(By.XPATH,'//*[@id="core-wrapper"]/section/div/div/div/div/div/form/button').click()
try:
    activate = driver.find_element(By.XPATH,'//*[@id="core-wrapper"]/section/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a')  # activate plan
    driver.execute_script("arguments[0].click();", activate)
except:
    print("[+]Plan is already activated.")
time.sleep(delay_action)

try:
    left_videos = int(driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[1]/h2/span/div').text)
    print(f'[+] {left_videos} videos [+]')
except:
    print("[X]You already used the program in the last 12 hours.")
    quit()

while left_videos:
    driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/a').click()
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="items"]/ytd-grid-video-renderer[1]').click()
    time.sleep(10)
    like_button = driver.find_element(By.XPATH,'//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').click()
    time.sleep(delay_action)
    print("[.] Following")
    sub_button = driver.find_element(By.XPATH,'//*[@id="subscribe-button"]/ytd-subscribe-button-renderer').click()
    time.sleep(delay_action)
    driver.implicitly_wait(2)
    driver.close()
    print("[.] Changing Page")
    time.sleep(delay_action)
    print("[.] Clicking continue...Wait!")
    driver.find_element(By.XPATH,'//*[@id="likeSub3"]/a').click()
    time.sleep(delay_popup)
    try:
        left_videos = int(driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[1]/h2/span/div').text)
        print(f'[+] {left_videos} videos [+]')

        print("[===========================================]")
        print("[...]Continuing cycle[...]")
    except:
        print("[===========================================]")
        print("No more videos left on SubPals.")
        print("[===========================================]")

        break

    time.sleep(2)
#quit()





















#            -------activation-------
#driver.find_element(By.XPATH,'//*[@id="core-wrapper"]/section/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a').click()
#while True:
#    #      ---click on  subscribe in subpals---
#    driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/a').click()
#    #         ---to click on random video---
#    driver.find_element(By.XPATH,'/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]').click()
#    #             ---pause the video---
#    driver.find_element(By.CLASS_NAME, "ytp-play-button ytp-button").click()
#    #           -----LIKE the video-----
#    driver.find_element(By.ID, 'interaction').click()
#    #           ---subscribe the video---

#    #           ---conform subscribed---

#sleep(5)
#driver.close() #it close the chrome tab
