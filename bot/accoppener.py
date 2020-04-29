
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import tinydb

db = tinydb.TinyDB("db/userlistdb_storage.json") 

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        addata = db.search(where('ad'))
        soyaddata = db.search(where('soyad'))
        sifredata = db.search(where('sifre'))
        maildata =db.search(where('mail'))

    def signIn(self):
        self.browser.get('https://www.instagram.com/')

        #fonx
        epostaInput = self.browser.find_elements_by_css_selector('form input')[0]
        adsoyadInput = self.browser.find_elements_by_css_selector('form input')[1]
        sifreInput = self.browser.find_elements_by_css_selector('form input')[3]
        #data

        #sendkeys moruk ya
        emailInput.send_keys(self.addata)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

 
