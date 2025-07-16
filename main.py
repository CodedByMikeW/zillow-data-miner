from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


responses =requests.get('https://appbrewery.github.io/Zillow-Clone/')
web=responses.text
soup=BeautifulSoup(web,"html.parser")


links=[]


All_links=soup.find_all(name="a",class_="property-card-link")
for loop in All_links:
    given=loop['href']
    links.append(given)
print(links)

Money=[]
All_money= soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
for loop in All_money:
    given=loop.text
    Money.append(given)
print(Money)

Address=[]

All_Address=soup.find_all(name="address")

for loop in All_Address:
    given=loop.text
    Address.append(given)
Clean_Address=[addr.strip() for addr in Address]
print(Clean_Address)


print(Address[0])

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfQwGfwkp4gJW24GtssJadDX2onEvSsKEaD0m4GXr9ma7U8XA/viewform?usp=header')
def MACHINE(Number):
    Address_p=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Address_p.send_keys(Clean_Address[Number])

    Money_p=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Money_p.send_keys(Money[Number])

    Links_p=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Links_p.send_keys(links[Number])

    Button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Button.click()


    Another=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    Another.click()

index=0

while index< len(links):
    MACHINE(index)
    time.sleep(1)


    index += 1


