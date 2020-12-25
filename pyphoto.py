# 需求:爬取图片

import json
import os  # 用于创建文件夹
import re

import requests

if __name__ == '__main__':
    # url='https://tva1.sinaimg.cn/bmiddle/0080xEK2gy1gbllrs5uzxj30kr0pjtbu.jpg'
    # #content返回的是二进制形式的图片数据
    # #text(字符串) content(二进制) json(对象)
    # img_data=requests.get(url=url).content

    # with open('./one.jpg' ,'wb' ) as fp:
    #   fp.write(img_data)
    # 创建文件夹保存所有图片
    if not os.path.exists('./mm'):
        os.mkdir('./mm')
    url = 'https://www.buxiuse.com/?cid=2&page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    # 使用通用爬虫对url对应的一整张页面进行爬取
# 有一个问题,不是page的问题是第二页的class类名改了

    page_data = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫对页面进行解析,和获取
    # 正则表达式
    ex = '<div class="img_single">.*?<img class.*? src="(.*?)" referrerpolicy.*?</div>'
    # re.findall(pattern, string, flags=0)pattern-->正则表达式 string-->需要处理的字符串 flags-->说明匹配模式，如是否大小写re.I 参数有re.S，不会对\n进行中断
    img_src_list = re.findall(ex, page_data, re.S)
    # print(img_src_list)
    i = 0
    for src in img_src_list:
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        imgname = str(i)+src.split('/')[-1]
        i = i+1
        # 图片存储路径
        imgpath = './mm/'+imgname
        with open(imgpath, 'wb') as fp:
            fp.write(img_data)
            print(imgname+'下载成功')

# 关于python学习中遇到的can only concatenate str （not “int”）to str 这种错误经过学习得到了以下结论:

# 1、字面上理解即只能用字符串与字符串拼接，笔者自己便是将int的数字与字符串拼接时得到这种报错
# 2、解决方式:根据需要转换数据类型
# 如:字符串转换为int int_data=int(str_data)
# nt 转换为字符串 str_data=str(int_data)
