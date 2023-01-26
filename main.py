from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

def img_generate(prompt, session_token, email):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    
    options.headless = True
    
    browser = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    browser.get('https://lexica.art/aperture')
    time.sleep(5)
    browser.add_cookie({'name': '__Secure-next-auth.session-token', 'value': session_token})
    
    lexica_prompt_edit = "-".join(prompt.split(" "))
    lexica_prompt_edit = lexica_prompt_edit.replace(",","")
    lexica_prompt_edit = lexica_prompt_edit.replace(".","")
    lexica_prompt_edit = lexica_prompt_edit.replace("'","")
    lexica_prompt_edit = lexica_prompt_edit.replace("*","")
    lexica_prompt_edit = lexica_prompt_edit.replace("\\n","")
    time.sleep(5)
    textspace = browser.find_element(By.XPATH, '//*[@id="main-generate"]')
    textspace.send_keys(prompt)
    button = browser.find_element(By.XPATH, '//*[@id="generate-button"]/button')
    button.click()
    time.sleep(2)
    email_inp = browser.find_element(By.XPATH, '//*[@id="radix-:r3:"]/div/form/input')
    email_inp.send_keys(email)
    browser.find_element(By.XPATH, '//*[@id="radix-:r3:"]/div/form/button').click()
    time.sleep(2)
    button.click()
    time.sleep(15)
    images = browser.find_elements(By.TAG_NAME, 'img')
    count = 0
    for image in images:
        count = count + 1
        url = image.get_attribute('src')
        response = requests.get(url)
        with open(lexica_prompt_edit + '_' + str(count) + '.jpg', 'wb') as f:
            f.write(response.content)
    browser.quit()

session_token = "xxxxxx"
img_generate("prompt", session_token, "abc@123.com")
