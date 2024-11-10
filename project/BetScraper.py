from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector

def database():
    db = mysql.connector.connect(host="localhost",
                                 user= "root",
                                 password= "",
                                 database= "")
    assert db.is_connected() == True

    func = db.cursor()
    return db

def chrome_driver():
    options = Options()
    #options.add_experimental_option("detch", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def scraper():
    driver = chrome_driver()
    driver.get("https://www.betway.co.zm")
    driver.maximize_window()
    try:
        #LOGIN
        number = "976019954"
        password = "VanZ7777"

        #IF THE POPUP PERSISTS
       # popup = driver.find_element("xpath", "//*[@id='close-toast']").click()

        #SECOND LOGIN POPUP
        {
            #some logic comes here
        }

    #LOCATING THE FORM
        user_num = driver.find_element("xpath", "//*[@id='header-username']")
        user_pass = driver.find_element("xpath", "//*[@id='header-password']")
        login_button = driver.find_element("xpath", "//*[@id='__nuxt']/div/div/div[1]/header/div/div[2]/div/button[1]")

    #CLICKING TO LOG IN
        user_num.send_keys(number)
        user_pass.send_keys(password)
        login_button.click()

        #BASKETBALL_EVENTS
        basketball_tab = driver.find_element("xpath", "//*[@id='sport-games-list-scroller']/div[4]/button")
        basketball_tab.click() #Switches to the basketball tab

    
        basketball_events = driver.find_elements("xpath","//div[@class='rounded_lg'") #Specifies the names and links of episodes
        events = []

        event_name = driver.find_elements("xpath", "//*[@id='14721451']/div/a")
        home_odds = driver.find_elements("xpath", "//*[@id='14721451']/div/div[1]/div[3]/div/div[1]")
        for event in basketball_events:
            events.append(event.get_attribute("innerHTML")) #Adds episode to the anime array
        return  events

    finally:
        driver.quit()

    def arbitrage():
        pass


    def auto_bet():
            pass

    return


if __name__ == '__main__':
    scr = scraper()
    print(scr)