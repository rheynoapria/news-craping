# -*- coding: utf-8 -*-
import scrapy
from newsDataset.items import NewsdatasetItem



class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tribunnews.com']
    start_urls = ['http://tribunnews.com/bisnis']

    def parse(self, response):
        for url in response.xpath("///h3/a/@href").extract():
            full_url = response.urljoin(url)
            # print("Found URL : "+full_url)
            yield scrapy.Request(full_url,callback=self.getdata)
        

    def getdata(self,response):
        paragraph=[]

        item = NewsdatasetItem()
        item['date'] =  response.xpath("normalize-space(//*[@id='article']/div[1]/time)").extract_first()
        item['title'] = response.xpath("normalize-space(//*[@id='arttitle']/text())").extract_first() 
        all_desc = response.css('div.side-article > p ::text').extract()  
        for i in range(len(all_desc)):
            a = str(all_desc[i])
            if a.isupper():
                continue
            elif a.endswith("."): 
                paragraph.append(all_desc[i])
                break
            elif a.startswith("L"):
                pass
            else:
                paragraph.append(all_desc[i])
        final = "".join(paragraph).split(" - ")  
        if len(final) > 1:
            final_desc = final[1]
        elif len(final) == 1:
            final_desc = final[0]
        # final_desc = response.xpath("normalize-space(//div[4]/p[2]/text())").extract()
        item['desc']  = final_desc
        text = response.xpath("normalize-space(//*[@id='article_con']/div[4]/p[2]/strong)").extract_first()
        text_split = text.split(", ")
        if (len(text_split)) == 2:
            item['location'] = text_split[1]
        if (len(text_split)) == 1:
            item['location'] = "null"
        item['category'] = 'Bisnis'
        item['source'] = 'Tribunnews.com'
        
        yield item
        
      