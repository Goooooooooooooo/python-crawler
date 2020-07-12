import requests as req
from bs4 import BeautifulSoup
import time
import codecs




headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Connection':'close'}


req.adapters.DEFAULT_RETRIES = 10
req.packages.urllib3.disable_warnings()
a = req.Session()
a.keep_alive = False


def get_contents(url):
    r = a.get(url, headers = headers, verify = False)

    print(r.status_code)
    print(r.url)

    soup = BeautifulSoup(r.content, 'html.parser')

    url_list = []

    list = soup.select('dd > a')

    for i in list:
        i = i.get('href')
        i = 'https://www.biqugecom.com/' + i
        url_list.append(i)
    url_list = url_list[9:-1]
    return url_list


def get_content(url):
    
    r = a.get(url, headers = headers, verify = False)
    time.sleep(0.5)
    
    soup = BeautifulSoup(r.content, 'html.parser')

    data = {}

    catalog = soup.select('h1')

    data['catalog'] = ''
    if len(catalog) > 0:
        data['catalog'] = catalog[0].text

    print(data['catalog'])
    
    content_list = soup.select('#content')
    data['content'] = ''
    for x in content_list:
        data['content'] = data['content'] + '\r\n' + x.text.replace('readx();','')
    return data


if __name__ == '__main__':

    url = 'https://www.biqugecom.com/22/22587/'
    fileName = 'J:\\Story\\崩坏世界的传奇大冒险.txt'
    url_list = get_contents(url)
    print(len(url_list))
    print(url_list)

    f = codecs.open(fileName, 'a+', 'utf-8')
    for i in url_list:
        data = get_content(i)
        f.write('\r\n' + data['catalog'] + '\r\n')
        f.write('\r\n' + data['content'] + '\r\n')
    f.close()





    
    
