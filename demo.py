# 1.找到指定url
# 2.发起请求
# 3.获取响应数据
# 4.持久化存储


import requests
import json


if __name__ == "__main__":
    # 找到指定url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    id_list = []
    all_data_list = []
    for number in range(1, 2):
        data = {
            'on': 'true',
            'page': number,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': ''}
    # 发起请求
        page_data = requests.post(url=url, data=data, headers=headers).json()
        # with open('test.json', 'w') as f:
        #     json.dump(page_data, f)
        # 获取响应数据
        for dic in page_data['list']:
            id_list.append(dic['ID'])
    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id,
        }
        # 发起请求
        detail_data = requests.post(
            url=post_url, data=data, headers=headers).json()
        # print(detail_data)
        # 获取响应数据
        all_data_list.append(detail_data)
        # 持久化存储
        with open('./all.json', 'w', encoding='utf-8') as fp:
            json.dump(all_data_list, fp, ensure_ascii=False)
