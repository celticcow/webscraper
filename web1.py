#!/usr/bin/python3

import requests
import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class SneakerBot:
    """
    """

    def __init__(self, url):
        self.sneaker_url = url
        binary = FirefoxBinary('/usr/bin/firefox')

        Op = Options()
        Op.add_argument('--headless')
        
        self.driver = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')#, options=Op)
        ##self.driver = webdriver.Firefox()
        #s = Service('./chromedriver')
        #self.driver = webdriver.Chrome(service = s)
    
    def get_price(self):
        is_on_sale = 0
        self.driver.get(self.sneaker_url)
        price = self.driver.find_element_by_xpath('//div[@data-test="product-price"]')
        try:
            sale = self.driver.find_element_by_xpath('//div[@data-test="product-price-reduced"]')
            
                                                             
            print("on sale")
            is_on_sale = 1
        except:
            pass

        if(is_on_sale):
            #return int(sale.get_attribute('innerHTML').strip('$'))
            #print("********")
            #print(sale.get_attribute('innerHTML').strip('$'))
            #print("\n")
            #print(price.get_attribute('innerHTML'))
            #print("********")

            return(float(sale.get_attribute('innerHTML').strip('$')))
        else:
            return float(price.get_attribute('innerHTML').strip('$'))

    def close_bot(self):
        self.driver.close()

##end of class


def main():
    print("begin")

    url = 'https://www.nike.com/t/kd13-chill-basketball-shoe-kbKpNV'
    url2 = 'https://www.nike.com/t/air-zoom-pegasus-37-flyease-mens-running-shoe-extra-wide-8nq874/CK8446-004'

    bot = SneakerBot(url)

    price = bot.get_price()

    print("Price is : ", end="")
    print(price)

    bot.close_bot()

if __name__ == "__main__":
    main()
