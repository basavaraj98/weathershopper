
from findproducts import AloeAlmond, SPF5030
from selenium import webdriver

browser=webdriver.Chrome()
browser.maximize_window()

browser.get("https://weathershopper.pythonanywhere.com/")
value =browser.find_element_by_xpath("//span[contains(@id,'temperature')]")
temp=int((value.text)[:-2])

if temp<19:
    browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]").click()
    AloeAlmond(browser)
elif temp>34:
    browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]").click()
    SPF5030(browser)






