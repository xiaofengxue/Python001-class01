# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector



class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    #start_urls = ['https://maoyan.com/films/1218273']
    start_urls = ['https://maoyan.com/films?showType=3']



    # def parse(self, response):
    #     # for i in range(1,11):
    #     #     print(i)
    #     #     item = MaoyanItem()
    #     #     # name = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()').extract_first()
    #     #     # types = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]//a[@class]/text()').extract()
    #     #     # release_time = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract()
            
    #     #     # item['name'] = name
    #     #     # item['types'] = types
    #     #     # item['release_time'] = release_time
    #     #     # yield item
    #     #     print(name)
    #     #     print(types)
    #     #     print(release_time)
    #     name = Selector(response=response).xpath('//dd/a[1]/@title').extract_first()
    #     print(name)
    def parse(self, response):
        item = MaoyanItem()
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies[0:10]:
            name = movie.xpath('.//span/text()').extract_first()
            types = movie.xpath('.//div[@class="movie-hover-title"]/text()').extract()[0:-1]
            release_time = movie.xpath('.//div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[-1].replace('\n','').replace(' ','')
            print(name)
            type_name = ''
            for type in types:
                type_name += type
            print(type_name.replace('\n','').replace(' ',''))
            print(release_time)
            item['name'] = name
            item['types'] = type_name.strip()
            item['release_time'] = release_time+'\n'
            yield item

   
      


                                


                                                    
