import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.maximize_window()

browser.get("https://weathershopper.pythonanywhere.com/")
value =browser.find_element_by_xpath("//span[contains(@id,'temperature')]")
temp=int((value.text)[:-2])
value=value.text

if temp<19:
    browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]").click()
    print(f"The weather seems cold ({value}), redirecting to moisturizers page")
elif temp>34:
    browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]").click()
    print(f"The weather seems hot ({value}), redirecting to sunscreens page")

list1=browser.find_elements_by_xpath("//*[contains(text(),'Aloe')]")
list2=browser.find_elements_by_xpath("//*[starts-with(., 'Price: ')]")
listofprices=[list[i].text for i in list1.text]
prices=[int(price[-3:]) for price in listofprices]
print(min(prices))
