from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# подключаем драйвер    
driver = webdriver.Firefox()
# открываем страницу
driver.get("http://abrams.ru/")

# По тегу считываем текст
txt = str(driver.find_element(By.TAG_NAME, "body").text)
print(txt)
print (f"\nСимволов в тексте: {len(txt)}")
# Возможно @ и еще некоторые символы он считает за 2 хз 
# но на спец сайте и в текст редакторе и в ворде считается поразному 
# с погрешностю +-10



d = {'Буквы': 0, 'Цифры': 0, 'Пробелы': 0, 'Спец.символы': 0}
for i in txt:
    if i.isalpha():
        d['Буквы'] += 1
    elif i.isdigit():
        d['Цифры'] += 1
    elif i == (" "):
        d['Пробелы'] += 1
    else:
        d['Спец.символы'] += 1

print(f"Пробелов в тексте: {d['Пробелы']} \nЗнаков в тексте: {len(set(txt))}")
# *Уникальных знаков
sleep(5)
driver.close()
driver.quit()






