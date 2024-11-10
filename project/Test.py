from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


def chrome_driver():
    options = Options()
    options.add_experimental_option('detch', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def scraper():
    driver = chrome_driver()
    driver.get("https://www.betway.co.zm/sport/basketball/highlights")
    driver.maximize_window()

    # LOGIN
    number = "976019954"
    password = "VanZ7777"

    user_num = driver.find_element("xpath", "//*[@id='header-username']")
    user_pass = driver.find_element("xpath", "//*[@id='header-password']")
    login_button = driver.find_element("xpath", "//*[@id='__nuxt']/div/div/div[1]/header/div/div[2]/div/button[1]")

    user_num.send_keys(number)
    user_pass.send_keys(password)
    login_button.click()

    return None


if __name__ == '__main__':
    scr = scraper()
    print(scr)