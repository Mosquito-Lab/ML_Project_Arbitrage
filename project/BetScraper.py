from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


def database():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="")
    assert db.is_connected() is True

    func = db.cursor()
    return db


def chrome_driver():
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def scraper():
    driver = chrome_driver()
    driver.get("https://www.betway.co.zm")
    driver.maximize_window()
    try:
        # LOGIN
        number = "976019954"
        password = "VanZ7777"

        # IF THE POPUP PERSISTS
        # popup = driver.find_element("xpath", "//*[@id='close-toast']").click()

        # LOCATING THE FORM IF IT INDEED POPS UP
        user_num = driver.find_element("xpath", "//*[@id='header-username']")
        user_pass = driver.find_element("xpath", "//*[@id='header-password']")
        login_button = driver.find_element("xpath", "//*[@id='__nuxt']/div/div/div[1]/header/div/div[2]/div/button[1]")

        # CLICKING TO LOG IN
        user_num.send_keys(number)
        user_pass.send_keys(password)
        login_button.click()

        # SECOND LOGIN POPUP
        second_user = driver.find_element("xpath", "//*[@id='login-mobile']")
        second_pass = driver.find_element("xpath", "//*[@id='login-password']")
        second_login = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div/div/form/div[2]/button")
        second_user.send_keys(number)
        second_pass.send_keys(password)
        second_login.click()

        # BASKETBALL_EVENTS
        basketball_tab = driver.find_element("xpath", "//*[@id='sport-games-list-scroller']/div[4]/button")
        basketball_tab.click()  # Switches to the basketball tab
        #

        basketball_events = driver.find_elements("xpath", "//*[@id='sports-container']/div[5]")  # Where the odds are

        events = []
        leagues = ['NBA, USA', 'NCAAB, USA', 'A1, Greece', 'NCAA Women, USA']
        for event in basketball_events:
            #if (basketball_events == "//span[contains(@class, 'overflow-hidden)][text()[contains(., 'NBA, USA')]]"):
            #else:
            events.append(event.get_attribute("innerHTML"))  # Parses the leagues and collects all data in text

        NBA = driver.find_elements("xpath", "//div[contains(@id, 'sports-container')][.//div[contains(@class, 'rounded-lg')]")
        return events

    finally:
        # driver.quit()
        pass

    def arbitrage():
        pass

    def auto_bet():
        pass

    return


if __name__ == '__main__':
    scr = scraper()
    print(scr)
