from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from kankandou.spiders import kandou_spider

from scrapy.utils.project import get_project_settings

spider = kandou_spider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
reactor.run()