# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    def process_item(self, item, spider):
        name = item['name']
        types = item['types']
        release_time = item['release_time']
        output = f'{name}|{types}|{release_time}'
        with open('./maoyan.csv','a+',encoding='utf8') as f:
            f.write(output)
        return item
