from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



# подключаем драйвер    
driver = webdriver.Firefox()
# открываем страницу
driver.get("https://smittenkitchen.com/")

def pars_tegs(index):

    #считываем текст статьи
    txt = str(driver.find_element(By.CLASS_NAME, "smittenkitchen-print-hide").text)
    #print(txt)
    
    #разбиваем массив тегов до удобного вида
    parss_tags = tags[index].split(", ")
    print (f"Tags in the blog: {parss_tags}")

    for i in txt.split():
        #доходим до одинаковой части всех статей и заканчиваем
        if i == 'PREVIOUSLY':
            break
        #проверяем наличие тэгов в строке    
        if parss_tags == []:
            print ("All tags are included in the text\n")
            return 0
         
        #парсим статью и сравниваем слова в тексте с тегами 
        k = 0
        for j in parss_tags:
            if i.upper() == j:
                print (f"Tag {j} is present in text")
                parss_tags.pop(k)
            k+=1

    
    print (f"This tags: {parss_tags} are not in the text \n")

    return 0


# собираем все тэги
read_tags =driver.find_elements(By.CLASS_NAME, "cat-links")
#разбиваем текст для удобств
tags = []
for i in read_tags:
    tags.append(i.text)
del tags[4:10]

# пребираем статьи
for i in range (2):
    
    items = driver.find_elements(By.CLASS_NAME, "entry-title")[i].click()

    pars_tegs(i)

    driver.back()

driver.close()
driver.quit()






