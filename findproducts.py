def AloeAlmond(browser):
    list1 = browser.find_elements_by_xpath(
        "//*[contains(text(),'Aloe') or contains(text(),'aloe')]/following-sibling::p")
    listofprices1 = [list1[i].text for i in range(len(list1))]

    price1 = [int(price[-3:]) for price in listofprices1]
    list2 = browser.find_elements_by_xpath(
        "//*[contains(text(),'Almond') or contains(text(),'almond')]/following-sibling::p")
    listofprices2 = [list2[i].text for i in range(len(list2))]
    price2 = [int(price[-3:]) for price in listofprices2]

    print(f"Aloe: {min(price1)} Almond: {min(price2)}")
    browser.find_element_by_xpath("//button[@onclick='goToCart()']").click()

def SPF5030(browser):
    list1 = browser.find_elements_by_xpath(
        "//*[contains(text(),'SPF-50') or contains(text(),'spf-50')]/following-sibling::p")
    listofprices1 = [list1[i].text for i in range(len(list1))]
    price1 = [int(price[-3:]) for price in listofprices1]

    list2 = browser.find_elements_by_xpath(
        "//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p")
    listofprices2 = [list2[i].text for i in range(len(list2))]
    price2 = [int(price[-3:]) for price in listofprices2]

    print(f"SPF50: {min(price1)} SPF30: {min(price2)}")
    browser.find_element_by_xpath("//button[@onclick='goToCart()']").click()