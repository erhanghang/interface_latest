#-*- coding:utf-8 -*-
#author:yupeng
import unittest
import requests
import urllib

class Test_QueryIns(unittest.TestCase):
    def setUp(self):
        '这是开始'

    def test001(self):
        'ceshi ******'
        url = "http://zzk.cnblogs.com/s/blogpost"
        par = {"Keywords": "中文"}  # 参数存字典
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                 "Cookie": "UM_distinctid=15d6981cb266f-084faa778153e4-c393062-15f900-15d6981cb271ba; _ga=GA1.2.1776787901.1500036947",
                  }
        res1 = requests.get(url=url, params=par, headers=header)
        print(res1.url)
        print(res1.encoding)
        print(urllib.parse.unquote(res1.url))  #

    def tearDown(self):
        '这是结束'

if __name__ == "__main__":
    Test_QueryIns()

