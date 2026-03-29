from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ROOT_FOLDER = Path(__file__).parent 
print(ROOT_FOLDER)
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'
print(CHROMEDRIVER_EXEC)

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    return browser

if __name__ == '__main__': 
    TIME2WAIT = 10
    options = '--headless' #opçao para realizar toda a operaçao com o navegador sem ele aparecer
    browser = make_chrome_browser()
    browser.get('https://br.search.yahoo.com/')

    #Esperar aparecer o input desejado
    search_input = WebDriverWait(browser,TIME2WAIT).until(
        EC.presence_of_element_located(
            (By.NAME,'p')
        )
    )
    search_input.send_keys('HELLO, WORLD!')
    search_input.send_keys(Keys.ENTER)


    #Quando tenho certeza que algo esta na tela
    results = browser.find_element(By.ID,'web')
    links = results.find_elements(By.TAG_NAME,'a')
    #print(links[0])
    links[0].click()

    sleep(TIME2WAIT)