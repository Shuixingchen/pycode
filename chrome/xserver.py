from selenium import webdriver

browser = webdriver.Chrome() 
browser.get(f"https://opensea.io/rankings")
selectors = browser.find_elements_by_xpath("//div[@role='listitem']")# 获得所有<div role="listitem">
for selector in selectors:
    print(22)
    title = selector.xpath("./div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX']").get()
    content = selector.xpath("./div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Ranking--collection-name-overflow']").get()
    print(title)
    print(content)
browser.close()