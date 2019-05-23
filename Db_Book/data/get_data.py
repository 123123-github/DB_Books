# http://119.29.3.47:9001/book/worm/isbn?isbn=9787533949358
# http://202.119.70.22:888/opac/openlink.php?strSearchType=isbn&strText=9787533949358
# URL = 'http://book.douban.com/isbn/9787533949358'
# 爬取豆瓣网的 书籍信息-书籍评论-评论用户 信息

import requests
from bs4 import BeautifulSoup
import data.spider
import models


# 豆瓣 api 通过 isbn 获取 book info - url
URL_TAG = 'https://book.douban.com/tag/'
URL_BOOK = 'https://book.douban.com/subject/'
URL_PEOPLE = 'https://www.douban.com/people/'
URL_COMMENT = 'https://book.douban.com/subject/4913064/comments/'
MAX_COMMENT = 200

tags = ['小说', '外国文学', '文学', '随笔', '中国文学', '经典', '日本文学', '散文']

# 获取书籍 url
def get_tag_books(url):
    text = data.spider.get_html_text(url)
    soup = BeautifulSoup(text, "html.parser")
    books = []
    for a in soup.select('.subject-item h2 a'):
        books.append(a['href'])
    return  books


# input: book_url
# 获取当前书籍信息
def get_book_info(url):
    text = data.spider.get_html_text(url)
    soup = BeautifulSoup(text, "html.parser")
    infos = soup.select_one('#info')

    book = models.Book()
    for info in infos.find_all('span'):
        attr = info.text.replace(' ', '').replace('\n', '') \
            .split(':')
        # 获取书籍属性值
        if attr[0] == '作者':
            book.authors = attr[1]
        elif attr[0] == 'ISBN':
            book.isbn = attr[1]
        elif attr[0] == '页数':
            book.pages = attr[1]
        elif attr[0] == '定价':
            book.price = attr[1]
    # 插入数据库
    book



# input: cur_isbn, subject_id
# 获取书籍评论信息 url_comments
def get_comments():

    pass


# input: isbn, user_list
# 获取评论用户信息 url_people
def get_user_info():

    pass


def main():
    # foreach in tag_list - foreach book in books
    # cur_book ->
    # 爬取书籍基本信息 - 存
    # 爬取书籍评论信息 - 存
    # 爬取评论用户信息 - 存


    pass


r = requests.get(TAG_URL, timeout=30)

print(r.text)




# 主过程
if __name__ == '__main__':

    for tag in tags:
        # 生成类别
        url_tag = URL_TAG + tag
        # 获取类别标签下的书籍 url
        books = get_tag_books(url_tag)
        for book in books:
            # 添加书籍信息，并返回书的标识 isbn
            isbn = get_book_info(book)
            # 添加评论信息 管理 isbn，同时返回 评论的用户
            users = get_comments(book, isbn)
            # 将涉及到的用户添加到系统
            get_user_info(isbn, users)





    pass