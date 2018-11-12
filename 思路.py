# 爬取全部城市PM2.5一年的数据

    # 1.第一层：全部城市    静态
    # https://www.aqistudy.cn/historydata/

    # 2.第二层：所有月份    动态数据
    # https://www.aqistudy.cn/historydata/monthdata.php?city=%E9%98%BF%E9%87%8C%E5%9C%B0%E5%8C%BA

    # 3.第三层：每天的数据   动态js    目标数据
    # https://www.aqistudy.cn/historydata/daydata.php?city=%E9%98%BF%E9%87%8C%E5%9C%B0%E5%8C%BA&month=201810

    # scrapy 自定义 可以解决动态js问题 下载器（selenium）



    # 第一层 解析所有成是的链接和名字

        # 城市链接：
        # city_link_list = '' + '/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a/@href'

        # 城市名称
        # city_name_list = '/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a/text()'

    # 第二层： 解析该城市所有月份信息

        # 月份链接
        # month_link_list = '' + ''/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li/a/@href'

    # 第三层，解析每天的数据

        # 获取每天数据

        # 获取所有行（每天） tr_list
        # tr_list = response.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr')

        # 从删除第一行（表头信息）
        # tr_list.pop[0]
        # for tr in tr_list[1:-1]:

            # 日期
            # date = tr.xpath'td/text()'.ex
            # AQI
            # 质量等级
            # PM2.5
            # PM10
            # SO2
            # CO
            # NO2
            # O3_8h