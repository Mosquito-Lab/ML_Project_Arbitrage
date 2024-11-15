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
        leagues = ['NBA, USA', 'NCAAB, USA', 'NCAA Women, USA']
        event_name, event_time, home_odds, away_odds = [], [], [], []
        for event in basketball_events:
            #if (basketball_events == "//span[contains(@class, 'overflow-hidden)][text()[contains(., 'NBA, USA')]]"):
            #else:
            events.append(event.get_attribute("innerHTML"))  # Parses the leagues and collects all data in text

        NBA = driver.find_elements("xpath", "//div[contains(@id, 'sports-container')][.//div[contains(@class, 'rounded-lg')]")
        def arbitrage():
            db = database()
            func = db.cursor()

            for x in db:
                home_arb = (1 / home_odds[x]) * 100
                away_arb = (1 / home_odds[x]) * 100
                investment = 0
                arbitrage = home_arb + away_arb

                if (arbitrage < 100):
                    arb_events = func.statement("SELECT * FROM events WHERE arbitrage < 100")
                    # Total profit gained from event
                    profit = (investment / arbitrage ) - investment
                    # Amount to bet on home odds
                    home_bet = (investment * home_arb) / arbitrage
                    # Amount to bet on away odds
                    away_bet = (investment * away_arb) / arbitrage


            return arb_events

        def auto_bet():
            arb = arbitrage()
            betslip = []
            balance = 0.0

            return betslip

    finally:
        driver.quit()
        return auto_bet()


if __name__ == '__main__':
    scr = scraper()
    print(scr)
