from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import os

channel_pass = "sujith12345"  # INSERT PASS YOUTUBE
my_email = "sujithsubs03@gmail.com"  # INSERT EMAIL GOOGLE
email_pass = "Sujith"  # INSERT PASSWORD EMAIL GOOGLE
user_data_dir = "C:\script folder\chromedriver.exe"  # C:\\Users\\{YOUR USER}\\AppData\\Local\\Google\\{YOUR CHROME}\\User Data\\Default
delay_action = 6  # delay for action
delay_popup = 40  # delay for get stats

script_folder = os.path.dirname(__file__)
driver_folder = os.path.join(script_folder, 'chromedriver.exe')


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


option = Options()

option.add_argument("--user-data-dir={}".format(user_data_dir))
option.add_argument('--profile-directory=Default')
option.headless = True  # FALSE = SHOW ACTION IN CHROME
driver = webdriver.Chrome(driver_folder, options=option)

url_sub = "https://www.subpals.com/login/final/UCcFrrU5HatzM6JNuQAjw-Ew/"
driver.get(url=url_sub)

driver.implicitly_wait(10)
# storing the current window handle to get back to dashbord
main_page = driver.current_window_handle # channel id
driver.find_element_by_name('password').send_keys(channel_pass)  # Channel password
driver.find_element_by_xpath("//button[@type='submit']").click()  # SUMBMIT
print("[+]Logged to SubPals.[+]")

try:
    activate = driver.find_element_by_xpath('/html/body/div/center[2]/div/div[1]/div[2]/form/div/a')  # activate plan
    driver.execute_script("arguments[0].click();", activate)
except:
    print("[+]Plan is already activated.")

time.sleep(delay_action)
try:
    left_videos = int(driver.find_element_by_id('remainingHint').text)
    print(f'[+] {left_videos} videos [+]')
except:
    print("[X]You already used the program in the last 12 hours.")
    quit()
while left_videos:
    driver.find_element_by_xpath("//*[@id='likeSub2']/a").click()
    for handle in driver.window_handles:
        if handle != main_page:
            yt_page = handle
    try:
        driver.switch_to.window(yt_page)
        print("[.] Changing Page")

    except:
        print("[X]Popup not found")
        quit()
    try:
        email = "sujithsubs03@gmail.com"
        password_in = "Sujith"
        driver.get(
            "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element(By.ID, "identifierId").send_keys(email)
        driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
        time.sleep(3)
        password_input = driver.find_element(By.NAME, "password").send_keys(password_in)
        #driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
        password_input.send_keys(Keys.RETURN)
    except:
        print(f"{bcolors.OKGREEN}[+] Logged to Youtube. [+]{bcolors.ENDC}")
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/a').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="items"]/ytd-grid-video-renderer[1]').click()
        time.sleep(10)
        # Like and Sub:
        print("[.] Enjoying")
        like_button = driver.find_element(By.XPATH,'//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').click()
        time.sleep(delay_action)
        print("[.] Following")
        sub_button = driver.find_element(By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer').click()
        time.sleep(delay_action)
        driver.implicitly_wait(2)
        print("[.] Changing Page")
        driver.switch_to.window(main_page)
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
quit()
