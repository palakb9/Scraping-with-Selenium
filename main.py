import selenium
import time
from selenium import webdriver
from selenium.webdriver.common import options

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument('--headless')
  options.add_argument("start-maximized")
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)

  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1]) # spliting when there's a space
  return output

def main():
  driver = get_driver()
  time.sleep(2) # Waiting for the page to load for 2 seconds
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]") # Finding the element using inspect
  return element.text

print(main())
print(clean_text(main()))