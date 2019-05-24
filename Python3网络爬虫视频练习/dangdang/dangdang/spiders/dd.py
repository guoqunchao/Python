# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg 1-cid4003844.html']

    def parse(self, response):
        item = DangdangItem()
        # response.xpath('').extract()
        item['title'] = response.xpath('//p[@name="title"]/a/@title').extract()
        item['comment'] = response.xpath('//a[@dd_name="单品评论"]/text()').extract()
        item['link'] = response.xpath('//p[@class="name"]/a/@href').extract()
        yield item
        '''
        print("当前爬取标题数量:",len(item['title']))
        print("当前爬取评论数量:",len(item['comment']))
        print("当前爬取商品链接:",len(item['link']))
        self.WriteFile(item)

    def WriteFile(self,item):
        if len(item['title']) == len(item['comment']):
            with open('dd_result.txt','w') as f:
                for i in range(0,len(item['title'])):
                    print(item['title'][i])
                    print(item['comment'][i])
                    f.write(item['title'][i]+"   "+item['comment'][i]+"   "+item['link'][i]+'\n')
        else:
            print('Warm：内容数量一致')
            exit()
        '''