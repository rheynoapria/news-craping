# -*- coding: utf-8 -*-
import scrapy
import re
import unicodedata
from newsDataset.items import TeknologiNewsItem

class TechNewsSpider(scrapy.Spider):
    name = 'tech-news'
    allowed_domains = ['idntimes.com']
    api_url = 'https://www.idntimes.com/ajax/category/tech?page={}'
    start_urls = [api_url.format(1)]
    page = 1
    num = 0

    def parse(self, response):
        a=0
        list_url = response.xpath('/html/body/div/a/@href').extract() 
        
        for i in range(len(list_url)-1):
            full_url = response.urljoin(list_url[i])
            yield scrapy.Request(full_url,callback=self.getdata)
        self.page = self.page + 1
        a = self.page + 1
        if(a<=20):
            yield scrapy.Request(url=self.api_url.format(a),callback=self.parse)

    def getdata(self, response):
        self.num = self.num + 1
        item = TeknologiNewsItem()
        url_text = response.request.url
        date_scrap = response.xpath('//*[@id="article-page"]/ol/li[3]/time/@datetime').extract()
        date = date_scrap[0]
        source = 'idntimes.com'

        # loc = response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/p[1]/strong)').extract() 
        # if len(loc) == 0:
        #     loc = response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/strong)').extract()
        # loc_split = loc[0].split(', ')                                                                                          
        # location = loc_split[0]

        title = response.xpath('//*[@id="article-page"]/div[1]/section/div[1]/h1/text()').extract()  
        title_strip = re.sub(',|:|/|"','',title[0])
        final_title = unicodedata.normalize("NFKD",title_strip)

        desc = desc = response.xpath('//*[@id="article-content"]/p[1]/text()').extract()  
        if len(desc) == 0 :
            desc = 'null'
        text_desc = desc[0]
        desc_strip = re.sub(',|!','',text_desc)
        final_desc = unicodedata.normalize("NFKD",desc_strip)


        # store data
        item ['id']= self.num
        item['title'] = final_title
        item['desc'] =  final_desc
        item['date'] = date
        item['source'] = source
        item['url'] = url_text
        item['category'] =  'Teknologi'

        yield item