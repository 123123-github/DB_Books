# 书籍
class Book:
    isbn = null
    title = null
    price = null
    pages = null
    authors = null


#用户
class User:
    # 属性
    uid = ''
    name = ''
    city = ''


# 评价 & 评论
class Comment:
    isbn = ''
    uid = ''
    score = 0.0
    content = ''