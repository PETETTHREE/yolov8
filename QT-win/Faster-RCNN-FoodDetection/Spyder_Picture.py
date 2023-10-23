# -*- coding:utf-8 -*-
#作者：猫先生的早茶
#时间：2019年5月22日

import requests
import re

main_url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=胡萝卜的炒菜图片'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
          'Referer':'https://www.baidu.com',}
name = 0

def get_html(url):
    '''下载网页'''
    html = requests.get(url=url,headers=header).text
    return html


def get_img_url(data):
    '''匹配出图片的url'''
    url_re = re.compile('"thumbURL":"(.*?)","replaceUrl"')
    url_list = url_re.findall(data)
    return url_list

def get_img(url):
    '''下载并保存图片'''
    global name
    name += 1
    file_name = 'foodpicture\\{}.jpg'.format(name)
    img = requests.get(url=url,headers=header).content
    with open(file_name,'wb') as save_img:
        save_img.write(img)


html = get_html(main_url)
url_list = get_img_url(html)
for url in url_list:
    get_img(url)
    print ("正在下载第{}张图片".format(name))

