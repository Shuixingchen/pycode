import cloudscraper
from lxml.html import fromstring

scraper = cloudscraper.create_scraper()
resp = scraper.get("https://opensea.io/rankings").text

file_object = open('demo.txt', 'w')
file_object.write(resp)
file_object.close( )

selector = fromstring(resp)
selectors = selector.xpath("//div[@role='listitem']") #获取所有的<div role="listitem">
for selector in selectors:
    print(22)
    title = selector.xpath("./div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX']").get()
    content = selector.xpath("./div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Ranking--collection-name-overflow']").get()
    print(title)
    print(content)