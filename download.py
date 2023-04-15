from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def download(url, path):
    # Create an instance
    options = Options()
    options.headless = False
    options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    driver = webdriver.Firefox(executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe", options=options)
    
    try:
        driver.get(url)

        try:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, path))
            )
            button.click()
        except Exception as e:
            print("Error:", e) 

        # Click the button
        button.click()

        # get the HTML source code
        html_code = driver.page_source
        print(html_code)
        
        #Kill browser
        driver.quit()
        
    except:
        #driver.quit()
        print("Error")



if __name__ == '__main__':
    #download(url = "https://www.swr.de/swr2/", path ="//button[@aria-label=' abspielen']")
    download(url="https://www.spiegel.de/", path="//button[@title='Akzeptieren und weiter']")