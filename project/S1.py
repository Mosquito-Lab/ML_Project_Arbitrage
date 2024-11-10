from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


def database():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="event_data")
    assert db.is_connected() == true #Checks if the DB is actually conencted to the script

    func = db.cursor() #Defines the use of SQL queries
    return db


def chrome_driver():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def scraper():
    driver = chrome_driver()
    driver.get("https://www.betway.co.zm/sport/basketball/highlights")

    def login():
        number = "976019954"
        password = "VanZ7777"

        user_num = driver.find_element("xpath", "//*[@id='header-username']")
        user_pass = driver.find_element("xpath", "//*[@id='header-password']")
        login_button = driver.find_element("xpath", "//*[@id='__nuxt']/div/div/div[1]/header/div/div[2]/div/button[1]")

        user_num.send_keys(number)
        user_pass.send_keys(password)
        login_button.click()

        return  None

    def basketball_events():
        # basketball_tab = driver.find_element("xpath", "//*[@id='sport-games-list-scroller']/div[4]/button")
        # basketball_tab.click() #Switches to the basketball tab

        try:
            basketball_events = driver.find_elements("xpath",
                                                     "//div[@class='rounded_lg'")  # Specifies the names and links of episodes
            events = []

            for event in basketball_events:
                events.append(event.get_attribute("innerHTML"))  # Adds episode to the anime array
            return events

        finally:
            pass  # driver.quit()

        return events

    def arbitrage():
        pass

    def auto_bet():
        pass

    return


if __name__ == '__main__':
    scr = scraper()
    print(scr)