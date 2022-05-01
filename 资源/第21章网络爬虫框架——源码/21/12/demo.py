from bs4 import BeautifulSoup  # 导入BeautifulSoup库

# 创建模拟HTML代码的字符串
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 创建一个BeautifulSoup对象，获取页面正文
soup = BeautifulSoup(html_doc, features="lxml")
print(soup)                  # 打印解析的HTML代码







