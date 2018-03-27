# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem


class QbspiderSpider(scrapy.Spider):
    pages =100
    name = "qbspider"
    allowed_domains = ["qiushibaike.com"]
    start_urls=[]

    for page in range(1,3):
        start_urls.append('https://www.qiushibaike.com/8hr/page/'+str(page)+'/')


    def parse(self, response):
        # for qiubaiItem in response.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]'):
        for qiubaiItem in response.xpath('//div[@id="content-left"]/div[contains(@class,"article block untagged mb15")]'):
            item = QiushibaikeItem()

            icon = qiubaiItem.xpath('./div[@class="author clearfix"]/a[1]/img/@src').extract()
            if icon:
                icon = icon[0]
                item['userIcon'] = icon.strip('\n')
            userName = qiubaiItem.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            if userName:
                userName = userName[0]
                item['userName'] = userName.strip('\n')

            content = qiubaiItem.xpath('./a[@class="contentHerf"]/div[@class="content"]/span/descendant::text()').extract()
            if content:
                con = ''
                for str in content:
                    con += str
                item['content'] = con.strip('\n')

            like = qiubaiItem.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()
            if like:
                like = like[0]
                item['like'] = like

            comment = qiubaiItem.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i/text()').extract()
            if comment:
                comment = comment[0]
                item['comment'] = comment.strip('\n')

            yield item
