from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3

PATH = "/Users/arunks/Desktop/Python_Studies/chromedriver" # Define chrome driver location
driver = webdriver.Chrome(PATH)  # Define object named driver

word = input("Find meaning of : ")

#driver.get('https://quotes.toscrape.com/')  # Open the website
driver.get('https://google.com/')


locator = 'input.gLFyf gsfi'
search = driver.find_element(By.CSS_SELECTOR,'div.L3eUgb input.gLFyf.gsfi')

search.send_keys(f'{word} meaning')
search.send_keys(Keys.RETURN)

meaning = driver.find_element(By.CSS_SELECTOR,'div.LTKOO.sY7ric').text

print(f"**********************Meaning of {word} ************************")
print(meaning)

speaker = pyttsx3.init()
speaker.say(meaning)
speaker.runAndWait()


driver.quit()   # close the website
