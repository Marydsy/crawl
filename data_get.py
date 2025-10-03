#爬取数据
import requests
import re
import pandas as pd

#请求目标链接中请求数据
def get_data(url,headers):
    try:
        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'
        data = str(response.text)#将获取的数据转换为字符串
    except:
        print('加载数据失败')
    return  data

#提取关键信息
def parse_data(data):
    name = (re.findall('univNameCn:"(.*?)".*?', str(data), re.S))#利用正则表达式提取需要的文本
    score = (re.findall('score:(.*?),.*?', str(data), re.S))
    result = []
    for i in range(len(name)):#将获取的数据合并
        result.append([i+1,name[i],score[i]])
    return result

#输出结果
def print_data(detail,num):#num表示需要输出的结果数
    tplt = "{0:^10}\t{1:^10}\t{2:^10}"
    print(tplt.format('排名', '学校名', '得分'))
    for item in range(num):
        temp =detail[item]
        print(tplt.format(temp[0],temp[1],temp[2]))

#将获取的结果保存到Excel中
def save_excel(detail,columns):
    file = pd.DataFrame(detail,columns=columns)
    file.to_csv('软科中国大学排名.csv',index=False)


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = 'https://www.shanghairanking.cn/_nuxt/static/1727343848/rankings/bcur/2024/payload.js'
    columns = ['排名','学校名称','软科总得分']
    row_data = get_data(url,headers)
    rank = parse_data(row_data)
    print_data(rank,200)#输出前200条数据
    save_excel(rank,columns)

if __name__=="__main__":
    main()

