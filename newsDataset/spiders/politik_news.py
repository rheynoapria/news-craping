# -*- coding: utf-8 -*-
import scrapy
from newsDataset.items import PolitikNewsItem
import unicodedata
import re

class PolitikNewsSpider(scrapy.Spider):
    name = 'politik-news'
    allowed_domains = ['gatra.com','antaranews.com']

    # gatranews
    api_gatra = 'https://www.gatra.com/rubrik/get_news?c=1&barisnya={}'
    # page = 10
    # num = 0
    
     # anatara news
    start_date = input('Enter Date for scraping (dd-mm-yyyy) = ')
    end_page = input('Enter End Page : ')
   
    api_url = 'https://www.antaranews.com/indeks/politik/{date}/{page}'
    start_urls = [api_url.format(date=start_date, page="")]
    page = 0
    num = 0

    def parse(self, response):
        # gatralisturl
        # a=10
        # list_url = response.xpath('///div[2]/p[1]/a/@href').extract()
        #   for i in range(len(list_url)):
        #     page = 0
        #     full_url = response.urljoin(list_url[i])
        #     yield scrapy.Request(full_url,callback=self.getdata) 
        #     page = page+i
        # self.page = self.page + page
        # a = self.page + page
        # if(a<=150):
        #     yield scrapy.Request(url=self.api_url.format(a),callback=self.parse)

        # antaralisturl
        a = 0 
        list_url = response.xpath('//*[@id="main-container"]/div[2]/div/div[1]/div[2]/div/article/header/h3/a/@href').extract() 
        for i in range(len(list_url)):
            page = 0
            full_url = response.urljoin(list_url[i])
            print('found url= '+full_url)
            yield scrapy.Request(full_url,callback=self.getdata_antara)
        self.page = self.page + 1
        a = self.page + 1
        endpage = int(self.end_page)
        if(a<=endpage):
            yield scrapy.Request(url=self.api_url.format(date=self.start_date, page=a),callback=self.parse)


    def getdata(self, response):
        self.num = self.num + 1
        item = PolitikNewsItem()
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
        item['category'] =  'Politik'

        yield item
        yield {
            'title' : response.xpath('//*[@id="content"]/div/div/div/div[1]/div/div/div/div/div[1]/text()').extract_first(),
            'desc' : response.xpath('normalize-space(//*[@id="content"]/div/div/div/div[3]/div[2]/div[2]/div/p[1]/text())').extract() 
        }
    
    def getdata_antara(self, response):
        self.num = self.num + 1
        item = PolitikNewsItem()

        url_text = response.request.url
        date = self.start_date
        source = 'antaranews.com'

        title = response.xpath('//*[@id="main-container"]/div[2]/div/div[1]/article/header/h1/text()').extract() 
        title_strip = re.sub(',|:|/|"','',title)
        final_title = unicodedata.normalize("NFKD",title_strip)

        



