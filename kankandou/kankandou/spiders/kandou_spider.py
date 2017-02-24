from scrapy.selector import Selector
from scrapy import Spider
from kankandou.items import KankandouItem
from scrapy.http import Request


class KanDouSpider(Spider):
    name = "kandou"

    def start_requests(self):
        for i in xrange(2, 432):
            yield Request("http://kankandou.com/book/page/{}".format(i), callback=self.parseBooks)

    def parseBooks(self, response):
        sel = Selector(response)
        details = sel.xpath("//div[@class='o-img']/a/@href")
        for d in details:
            uri = d.extract()
            print(uri)
            yield Request(url=uri, callback=self.parse_list)

    def parse_list(self, response):
        sel = Selector(response)
        blist = sel.xpath("//ul[@class='files']//a/@href")
        for b in blist:
            uri = b.extract()
            print(uri)
            yield Request(url=uri, callback=self.read_content)

    def read_content(self, response):
        file_name = response.headers.get("Content-Disposition").split(";")[1].split("=")[1].replace('"', '')
        content = bytes(response.body)
        item = KankandouItem()
        item['name'] = file_name
        item['file'] = content
        return item
