# import unittest
from time import sleep
#from multiprocessing import Pool as pool
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


#костыль для парсинга
words = "1 2 3 4 5 6 7 8 9 а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю a b c d e f g h i j k l m n o p q r s t u v w x y z"


#считывем ссылки
links = []
f = open("links.txt", "r")
try:
    for line in f:
        links.append(line)
finally:
    f.close()

# сортируем по длине
def sortByLength(inputStr):
        return len(inputStr)

links.sort(key=sortByLength)
    
# подключаем драйвер    
driver = webdriver.Firefox()

# перебираем ссылки и открывем в окне
for i in range(len(links)):  
    driver.get(links[i])
    if i != len(links)-1:
        driver.switch_to.new_window('tab')

 
k = 0 
# перебираем алфавит ища скходство с первой буквой заголовка 
for i in words:
    if k == len(links):
        break 
    x=0 # это нужно было делать чтобы не выходило за границы дозволенного
    for j in range(len(links)-k):
        driver.switch_to.window(driver.window_handles[j-x])
        urlTitel = driver.title  # считываем заголовок лол
        if i == urlTitel[0].lower():
            driver.close()
            k+=1
            x+=1 
    

sleep(5)
driver.quit()






