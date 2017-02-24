# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KankandouPipeline(object):

    def process_item(self, item, spider):
        abs_path = "/Users/spark/Downloads/kandou/"
        file = item['name'].decode("utf-8")
        with open(name=abs_path + file,mode='w') as f:
            f.write(str(item['file']))
        return item
