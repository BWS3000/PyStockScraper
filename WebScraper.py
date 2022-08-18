import os
import time
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium import webdriver

#Clear console
os.system('CLS')

"""
***How to hide a window***
url = "https://youtube.com"
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options) #Make sure to add the options to the webdriver
driver.get(url)
"""
stockPriceDict = {}
reload = True

def scrapeStockPrice(stockName):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    url = "https://www.tradingview.com/symbols/" + stockName +"/"
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    #Waits for the text within stockPrice element to load. 
    #Uses a '.' to determine if the <span> tag has been loaded
    try:
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span'), "."))
        stockPrice = driver.find_element(By.XPATH, '//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span').text
        stockPriceDict[stockName] = stockPrice
    except:
        return "-1"
    
    return stockPrice

def refreshAllPrices():
    for stock in stockPriceDict:
        stockPriceDict[stock] = scrapeStockPrice(stock)

def getStockPriceDict():
    return stockPriceDict
