# -*- coding: utf-8 -*-
import scrapy
import unicodedata
import re
from newsDataset.items import HukumNewsItem

class HukumNewsSpider(scrapy.Spider):
    name = 'hukum-news'
    allowed_domains = ['gatra.com']
    api_url = 'https://www.gatra.com/rubrik/get_news?c=81&barisnya={}'
    start_urls = [api_url.format(10)]
    page = 10
    num = 0

    def parse(self, response):
        a=10
        list_url = response.xpath('///div[2]/p[1]/a/@href').extract()
        
        for i in range(len(list_url)):
            page = 0
            full_url = response.urljoin(list_url[i])
            yield scrapy.Request(full_url,callback=self.getdata) 
            page = page+i
        self.page = self.page + page
        a = self.page + page
        if(a<=150):
            yield scrapy.Request(url=self.api_url.format(a),callback=self.parse)

    def getdata(self, response):
        self.num = self.num + 1
        item = HukumNewsItem()
        url_text = response.request.url
        time = response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[1]/div/div/div/div/div[2]/text())').extract()
        time_split = time[0].split(' | ')
        date = time_split[1]
        source = time_split[0]

        # loc = response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/p[1]/strong)').extract() 
        # if len(loc) == 0:
        #     loc = response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/strong)').extract()
        # loc_split = loc[0].split(', ')                                                                                          
        # location = loc_split[0]

        title = response.xpath('//*[@id="content"]/div/div/div/div[1]/div/div/div/div/div[1]/text()').extract_first()
        title_strip = re.sub(',|:|/|"','',title)
        final_title = unicodedata.normalize("NFKD",title_strip)

        desc = response.xpath('//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/p[1]/text()').extract()
        if len(desc) == 0 :
            desc = response.xpath('//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/text()').extract()
        text_desc = desc[0]
        desc_strip = re.sub('– |–| - |- |,|:|/|-','',text_desc)
        final_desc = unicodedata.normalize("NFKD",desc_strip)

        # desc_split = desc[0].split('- ')
        # if (len(desc_split)) > 1 :
        #     final_desc = unicodedata.normalize("NFKD",desc_split[1])
        # elif (len(desc_split)) == 1:
        #     final_desc = unicodedata.normalize("NFKD",desc_split[0])

        # store data
        item ['id']= self.num
        item['title'] = final_title
        item['desc'] =  final_desc
        item['date'] = date
        item['source'] = source
        item['url'] = url_text
        item['category'] =  'Hukum'

        yield item
        # yield {
        #     'title' : response.xpath('//*[@id="content"]/div/div/div/div[1]/div/div/div/div/div[1]/text()').extract_first(),
        #     'desc' : response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/p[1]/text())').extract() 
        # }