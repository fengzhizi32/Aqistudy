# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqistudyItem(scrapy.Item):

    # 城市名字
    city_name =scrapy.Field()

    # 日期
    date =scrapy.Field()
    # AQI
    aqi =scrapy.Field()
    # 质量等级
    level =scrapy.Field()
    # PM2.5
    pm2_5 =scrapy.Field()
    # PM10
    pm_10 =scrapy.Field()
    # SO2
    so2 =scrapy.Field()
    # CO
    co =scrapy.Field()
    # NO2
    no2 =scrapy.Field()
    # O3
    o3 =scrapy.Field()

    # 爬取的时间
    crawl_time =scrapy.Field()
    # 爬虫名字
    spider =scrapy.Field()