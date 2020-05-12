import re
import requests
from bs4 import BeautifulSoup

def open_file(file,x):
    openfile = open(file,x, encoding='utf-8')
    if x == 'r':
        return openfile.read()

class Request():
    def __init__(self, req):
        self.req = req

class Email(Request):
    def email(self):
        text = self.req
        return re.findall(r'\S*[@]\S+[.]\S+',text)

class English(Request):
    def eng_name(self):
        filter = re.findall(r'[^.!?:—][ ][A-Z]\w+',self.req)
        filter2 = ''
        for i in filter:
            filter2 = filter2 + ' ' + i
        listdubl = re.findall(r'[A-Z]\w+' , filter2)
        listchek = []
        for name in listdubl:
            if name not in listchek:
                listchek.append(name)
        return listchek

class Russian(Request):
    def ru_name(self):
        filter = re.findall(r'[^.!?:—][ ][А-Я]\w+',self.req)
        filter2 = ''
        for i in filter:
            filter2 = filter2 + ' ' + i
        listdubl = re.findall(r'[А-Я]\w+' , filter2)
        listchek = []
        for name in listdubl:
            if name not in listchek:
                listchek.append(name)
        return listchek

class HTML(Request):
    def get_html(self):
        page = requests.get(self.req)
        page.encoding = 'utf8'
        return page.text
    def get_content(self):
        html = requests.get(self.req).content
        return BeautifulSoup(html, 'lxml').text
    def get_lenta(self):
        soup = BeautifulSoup(self.req, 'lxml')
        head = soup.findAll('div', class_='card-mini__title')
        time = soup.findAll('time', class_='card-mini__date')
        url = soup.findAll('a',class_ = 'card-mini')
        heads = []
        for i in range(len(head)):
            if head[i] is not None:
                heads.append(time[i].text + ' ' + head[i].text + ' lenta.ru' + url[i].get('href'))
        return heads
    def get_url(self):
        filter = re.findall(r'\b[https://www.]+\w+[.]\w{2,3}\S+\b|\w+[.]\D{2,3}\b',self.req)
        filter2 = ''
        for i in filter:
            filter2 = filter2 + ' ' + i
        listdubl = re.findall(r'\b\w+[.]\w{2,3}\S+\b|\w+[.]\D{2,3}\b' , filter2)
        listchek = []
        for name in listdubl:
            if name not in listchek:
                listchek.append(name)
        return listchek
    
    
    if __name__=='__main__':
        file = open_file('C:/Users/Anton/Desktop/Python_course/Project/Article.txt','r')
        print(re.findall(r'[A-Za-z]+',file))
        html = 'http://vyshivayu.ru/spisok-uchastnikov-konkursa-krossvordov'
        print(HTML(html).get_content())
        print('Eng Name:',English(file).eng_name())
        print('Rus Name:',Russian(file).ru_name())
    
