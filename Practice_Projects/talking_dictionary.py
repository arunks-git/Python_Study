from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3

PATH = "/Users/arunks/Desktop/Python_Studies/Practice_Projects/chromedriver"  # Define chrome driver location
driver = webdriver.Chrome(PATH)  # Define object named driver
listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate' , 160)
#voices = speaker.getProperty('voices')
#speaker.setProperty('voice' , voices[1].id)


def take_command():
    try:
        with sr.Microphone() as source:
            speaker.say('What you want to search')
            speaker.runAndWait()
            print("Speak please....")
            voice = listener.listen(source, timeout=4, phrase_time_limit=4)
            word = listener.recognize_google(voice)
            print(word)
    except:
        print("Cant recognize")
    return word


#word = input("Find meaning of : ")
def get_result(word2):
    try:
        #driver.get('https://quotes.toscrape.com/')  # Open the website
        driver.get('https://google.com/')
        locator = 'input.gLFyf gsfi'
        search = driver.find_element(By.CSS_SELECTOR,'div.L3eUgb input.gLFyf.gsfi')
        search.send_keys(f'{word2} meaning')
        search.send_keys(Keys.RETURN)
        meaning = driver.find_element(By.CSS_SELECTOR,'div.LTKOO.sY7ric').text
        print(f"**********************Meaning of {word2} ************************")
        print(meaning)
    except:
        meaning = 'Sorry , I couldnt find it for you'
        print(meaning)
    return meaning

def read_result(meaning):
    speaker = pyttsx3.init()
    speaker.say(meaning)
    speaker.runAndWait()

word1 = take_command()
meaning = get_result(word1)
read_result(meaning)


driver.quit()   # close the website
