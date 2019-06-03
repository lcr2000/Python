#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 22:04
# @Author  : fangguizhen
# @FileName: demo.py
# @Software: PyCharm

import requests
from lxml import etree
# 导入csv
import csv
# 词云
from wordcloud import WordCloud
keyword = input("输入你要查询的工作：")
temp = r"C:\Users\Administrator\Desktop"+'\\'+ keyword
with open(temp + '.csv', 'a', newline='') as f:
    csvwriter = csv.writer(f, dialect='excel')
    csvwriter.writerow(["工作岗位", "公司名字", "公司位置", "工资", "发布时间"])
string = ''
# 一直访问下一页
next_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html'.format(keyword,1)
while next_url:
    response = requests.get(next_url)
    response.encoding = 'gbk'
    responsed = response.text
    # 格式转换
    html = etree.HTML(responsed)
    work_name = html.xpath('//div[@id="resultList"]/div[@class="el"]/p/span/a/@title')
    print(work_name)
    company_name = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t2"]/a/@title')
    print(company_name)
    company_location = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t3"]/text()')
    print(company_location)
    salary = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t4"]/text()')
    print(salary)
    date = html.xpath('//div[@id="resultList"]/div[@class="el"]/span[@class="t5"]/text()')
    print(date)
    # 判断是否超过索引
    try:
        next_url = html.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a/@href')[0]
    except IndexError as e:
        break
    # 使用内置函数zip
    for a,b,c,d,e in zip(work_name, company_name, company_location, salary, date):
        #  通过修改a,b,c,d,e的值生成不同的词云
        string += d + ''
        print(a,b,c,d,e)
        # 保存
        with open(temp + '.csv','a',newline='') as f:
             csvwriter = csv.writer(f,dialect='excel')
             csvwriter.writerow([a,b,c,d,e])

# 制作词云
wc = WordCloud(
    font_path = "simhei.ttf",
    background_color = 'white',
    # 允许最大最小的字体
    max_font_size = 70,
    min_font_size = 15,
    # 图片的宽高度
    width = 800,
    height = 600
).generate(string)
wc.to_file('test.png')