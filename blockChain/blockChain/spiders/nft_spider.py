import scrapy


class NftSpiderSpider(scrapy.Spider):
    name = 'nft_spider'
    allowed_domains = ['opensea.io']
    start_urls = ['https://api.opensea.io/tokens/?limit=100']
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

    def parse(self, response): #下载器返回response
        selectors = response.xpath("//div[@class='AnonymousHome_home__timeline__item_3vU']") #获取所有的<div role="listitem">
        for selector in selectors:
            title = selector.xpath("./h3/a/text()").get()
            content = selector.xpath('./p/text()').get()
            print(title)

