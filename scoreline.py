import re
import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict, deque

def normalInfo(year):
    if year == 2017:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/2116.htm'
    elif year == 2016:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1103.htm'
    elif year == 2015:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1117.htm'
    else:
        return '只支持15至17年'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    if year != 2015:
        rowsHtml = soup.find_all('tr', attrs={'class': False})
    else:
        rowsHtml = soup.find_all('tr', attrs={'class': False})[1:]
    index = ['年份', '类型', '省份', '科类', '专业', '录取分数线', '超一本线', '文化最低', '专业最低', '综合分最低']
    value = deque()
    for rowHtml in rowsHtml:
        if year != 2015:
            infos = rowHtml.find_all('td')
        else:
            infos = rowHtml.find_all('td', attrs={'class': re.compile(r'xl6[89]')})
        infoList = [year]
        infoList.append('普通文理')
        [infoList.append(info.get_text()) for info in infos]
        infoList.append('')
        infoList.append('')
        infoList.append('')
        dictionary = OrderedDict((zip(index, infoList)))
        value.append(json.loads(json.dumps(dictionary.copy())))
    return list(value)


def musiceInfo(year):
    if year == 2017:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/2121.htm'
    elif year == 2016:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1107.htm'
    elif year == 2015:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1102.htm'
    else:
        return '只支持15至17年'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    rowsHtml = soup.find_all('tr', attrs={'class': False})
    index = ['年份', '类型', '省份', '科类', '专业', '录取分数线', '超一本线', '文化最低', '专业最低', '综合分最低']
    value = deque()
    if year == 2015:
        rowsHtml = rowsHtml[1:]
    for rowHtml in rowsHtml:
        infos = rowHtml.find_all('td')
        dictionary = OrderedDict()
        for count in range(len(index)):
            if count == 0:
                dictionary[index[count]] = year
            elif count == 1:
                dictionary[index[count]] = '音乐专业'
            elif count == 2:
                dictionary[index[count]] = infos[0].get_text().strip()
            elif count == 3:
                dictionary[index[count]] = '艺术类'
            elif count == 4:
                dictionary[index[count]] = infos[1].get_text().strip()
            elif count in [5, 6]:
                dictionary[index[count]] = ''
            elif count == 7:
                dictionary[index[count]] = infos[2].get_text().strip()
            elif count == 8:
                dictionary[index[count]] = infos[3].get_text().strip()
            elif count == 9:
                dictionary[index[count]] = infos[4].get_text().strip()
        value.append(json.loads(json.dumps(dictionary.copy())))
    return list(value)


def artInfo(year):
    if year == 2017:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/2120.htm'
    elif year == 2016:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1106.htm'
    elif year == 2015:
        url = 'http://zhaosheng.cug.edu.cn/info/1012/1115.htm'
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        rowsHtml = soup.find_all('tr', attrs={'class': False})
        index = ['年份', '类型', '省份', '科类', '专业', '录取分数线', '超一本线', '文化最低', '专业最低', '综合分最低']
        value = deque()
        if year == 2015:
            rowsHtml = rowsHtml[1:]
        for rowHtml in rowsHtml:
            infos = rowHtml.find_all('td')
            dictionary = OrderedDict()
            for count in range(len(index)):
                if count == 0:
                    dictionary[index[count]] = year
                elif count == 1:
                    dictionary[index[count]] = '美术专业'
                elif count == 2:
                    dictionary[index[count]] = infos[0].get_text().strip()
                elif count == 3:
                    dictionary[index[count]] = '艺术类'
                elif count == 4:
                    dictionary[index[count]] = infos[1].get_text().strip()
                elif count in [5, 6]:
                    dictionary[index[count]] = ''
                elif count == 7:
                    dictionary[index[count]] = infos[2].get_text().strip()
                elif count == 8:
                    dictionary[index[count]] = infos[3].get_text().strip()
                elif count == 9:
                    dictionary[index[count]] = infos[4].get_text().strip()
            value.append(json.loads(json.dumps(dictionary.copy())))
        return list(value)
    else:
        return '只支持15至17年'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    rowsHtml = soup.find_all('tr', attrs={'class': False})
    index = ['年份', '类型', '省份', '科类', '专业', '录取分数线', '超一本线', '文化最低', '专业最低', '综合分最低']
    province = [
        '浙江', '山东', '山西', '河北', '陕西', '湖南', '湖北',
        '广西', '重庆', '四川', '江苏', '天津', '河南', '广东',
        '安徽', '云南', '江西', '福建'
    ]
    value = deque()
    rowspan = 4
    num = 0
    for rowHtml in rowsHtml:
        if rowspan == 0:
            rowspan = 4
            num += 1
        infos = rowHtml.find_all('td', attrs={'rowspan': False})
        dictionary = OrderedDict()
        for count in range(len(index)):
            if count == 0:
                dictionary[index[count]] = year
            elif count == 1:
                dictionary[index[count]] = '美术专业'
            elif count == 2:
                dictionary[index[count]] = province[num]
                rowspan -= 1
            elif count == 3:
                dictionary[index[count]] = '艺术类'
            elif count == 4:
                dictionary[index[count]] = infos[0].get_text().strip()
            elif count in [5, 6]:
                dictionary[index[count]] = ''
            elif count == 7:
                dictionary[index[count]] = infos[1].get_text().strip()
            elif count == 8:
                dictionary[index[count]] = infos[2].get_text().strip()
            elif count == 9:
                dictionary[index[count]] = infos[3].get_text().strip()
        value.append(json.loads(json.dumps(dictionary.copy())))
    return list(value)
