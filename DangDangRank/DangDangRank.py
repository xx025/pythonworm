import re
from time import sleep
from urllib.request import Request, urlopen

import xlwings as xw
from bs4 import BeautifulSoup
from requests import RequestException

headers = {
    'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': ' gzip, deflate',
    'Accept-Language': ' zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': ' max-age=0',
    'Connection': ' keep-alive',
    'Cookie': ' ddscreen=2; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20201205194104160290772419504871801; __rpm=...1607168495738%7C...1607168502004',
    'DNT': ' 1',
    'Host': ' bang.dangdang.com',
    'Upgrade-Insecure-Requests': ' 1',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_one_page(url_, headers_):
    req = Request(url=url_, headers=headers_, method='POST')
    try:
        response = urlopen(req)
        if response.getcode() == 200:
            return response.read()
        return None
    except RequestException:
        return None


class BOOK:
    def __init__(self, book):
        self.book = book

    # def getlist_num(self):
    #     listNum = 0
    #     try:
    #         listNum = self.book.find_all(attrs={"class": "list_num"})[0].text
    #     except:
    #         pass
    #     return listNum

    def getBookName(self):
        # 书名
        BookName = ""
        try:
            BookName = self.book.find_all(name='div', attrs={"class": "name"})[0].text
        except:
            pass
        return BookName

    def getBookAuthor(self):
        BookAuthor = ""
        # 作者
        try:
            strs = str(self.book.find_all(attrs={"class": "publisher_info"})[0]).replace('\n', '').replace('\r', '').replace(' ', '')
            print(strs)
            BookAuthor = re.findall("key=(.*?)\"", strs)[0]
        except:
            pass
        return BookAuthor

    def getBookPublisher(self):
        # 出版社
        BookPublisher = ""
        try:
            BookPublisher = self.book.find_all(attrs={"class": "publisher_info"})[1].find_all("a")[0].text
        except:
            pass
        return BookPublisher

    # def getBookPublisherTime(self):
    #     # 出版时间
    #     BookPublisherTime = ""
    #     try:
    #         BookPublisherTime = self.book.find_all(attrs={"class": "publisher_info"})[1].find_all("span")[0].text
    #     except:
    #         pass
    #     return BookPublisherTime

    def getInfo(self):
        return [self.getBookName(), self.getBookAuthor(), self.getBookPublisher()]


if __name__ == '__main__':
    list_book_rank = []
    url = 'http://bang.dangdang.com/books/bestsellers/1-'
    for i in range(1, 20):
        url_i = url + str(i)
        print(url_i)
        html = get_one_page(url_i, headers)
        soup = BeautifulSoup(html, "lxml")
        bang_list = soup.find_all(name='ul', attrs={"class": 'bang_list clearfix bang_list_mode'})[0]
        # print(bang_list)
        for j in bang_list.findAll(name="li"):
            thisbookinfo = BOOK(j).getInfo()
            if thisbookinfo[1] != "" and thisbookinfo[2] != "":
                list_book_rank.append(thisbookinfo)
        sleep(4)  # 休息2秒
    wb = xw.Book()
    sht = wb.sheets['Sheet1']
    sht.range('a1').value = ['书名', '作者', '出版社']
    sht.range('a2').value = list_book_rank
    wb.save(r'C:\Users\sun\Desktop\图书榜单.xlsx')#保存到桌面
