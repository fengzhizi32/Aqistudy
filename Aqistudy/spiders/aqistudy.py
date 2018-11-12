# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

from Aqistudy.items import AqistudyItem


class AqistudySpider(scrapy.Spider):
    name = 'aqistudy'
    allowed_domains = ['sqistudy.cn']
    base_url = 'https://www.aqistudy.cn/historydata/'
    # 发送首页的请求 获取全部的城市
    start_urls = [base_url]

    # 解析 所有城市名字和链接
    def parse(self, response):
        print('第一层')

        # 城市链接：
        city_link_list = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a/@href').extract()[10:11]
        # 城市名称
        city_name_list = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a/text()').extract()[10:11]

        for city_name, city_link in zip(city_name_list, city_link_list):
            item = AqistudyItem()
            item['city_name'] = city_name

            # 发送 城市链接请求
            city_url = self.base_url + city_link
            print('城市链接为：%s'% city_url)
            yield scrapy.Request(city_url, callback=self.parse_month, meta={'aqistudy': item})
        print('一层完')

    # 解析 所有的月份链接
    def parse_month(self, response):
        print('第二层')

        # 接收从首页 传入的item
        item = response.meta['aqistudy']

        # 月份链接
        month_link_list = response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li/a/@href').extract()[5:6]

        for month_link in month_link_list:
            month_url = self.base_url + month_link
            print('月份链接为：%s' % month_url)
            yield scrapy.Request(month_url, callback=self.parse_day, meta={'aqistudy': item})
        print('二层完')

    # 解析 每一天的数据
    def parse_day(self, response):
        print('第三层')

        # 接收从第二页 传入的item
        item = response.meta['aqistudy']

        # 取出所有行
        tr_list = response.xpath('//tr')

        # 删除表头 第一行
        tr_list.pop(0)

        # 遍历每一行的数据
        for tr in tr_list:

            # 日期
            item['ate'] = tr.xpath('td[1]/text()').extract_first()
            # AQI
            item['aqi'] = tr.xpath('td[2]/text()').extract_first()
            # 质量等级
            item['level'] = tr.xpath('td[3]/span/text()').extract_first()
            # PM2.5
            item['pm2_5'] = tr.xpath('td[4]/text()').extract_first()
            # PM10
            item['pm_10'] = tr.xpath('td[5]/text()').extract_first()
            # SO2
            item['so2'] = tr.xpath('td[6]/text()').extract_first()
            # CO
            item['co'] = tr.xpath('td[7]/text()').extract_first()
            # NO2
            item['no2'] = tr.xpath('td[8]/text()').extract_first()
            # O3
            item['o3'] = tr.xpath('td[9]/text()').extract_first()

            # item-->engine-->pipeline
            yield item

