from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def chrome_driver():
    options = Options()
    #options.add_argument("--headless") #No popup
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options= options)
    return driver
def scraper():
    driver = chrome_driver()
    driver.get("https://betpawa.co.zm") #site to be scraped
    driver.maximize_window()

    try:
        latest_odds = driver.find_elements("xpath"," ") #Specifies the names and links of episodes
        betting_data = []
        for anime in latest_odds:
            betting_data.append(anime.get_attribute("innerHTML")) #Adds episode to the anime array
        return betting_data

    finally:
        driver.quit()


if __name__ == '__main__':
    scr = scraper()
    print(scr)