import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("가격이 궁금한 책의 제목을 3개 입력하시오(콤마로 구분할 것)")
print('ex: 이기적 유전자,사피엔스,아몬드')
book_list=input(">>").split(',')
#print(book_list)

URL= 'http://www.yes24.com/main/default.aspx?ysmchn=ggl&ysmcpm=google-sponsor&ysmtac=ppc&ysmtrm=yes24&pid=123487&cosemkid=go14913756274066498&gclid=CjwKCAjwhYOFBhBkEiwASF3KGQFEKHh__pi6pXXOU0zI2lL9PZFXwpaiB8s8Ueu5UozPjGEgrFlE5RoCioQQAvD_BwE'
driver=webdriver.Chrome()
driver.get(url=URL)
author_list=[]

for book in book_list:
    driver.find_element_by_css_selector('#query.iptTxt').send_keys(book)
    driver.find_element_by_css_selector('#query.iptTxt').send_keys(Keys.ENTER)
    driver.find_element_by_class_name('img_bdr').click()

    author = driver.find_element_by_class_name('gd_auth').text
    author_list.append(author)

    time.sleep(3)

book_dic=dict()
for i in range(3):
    book_dic[book_list[i]]=author_list
print(book_dic)
for title,author in book_dic.items():
    print(title,'-',author)