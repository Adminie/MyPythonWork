from bs4 import BeautifulSoup  # 导入BeautifulSoup库

# 创建BeautifulSoup对象打开需要解析的html文件
soup = BeautifulSoup(open('index.html'), 'lxml')
print(soup.prettify())  # 打印格式化后的代码
