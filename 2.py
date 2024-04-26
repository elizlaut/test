from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import matplotlib.pyplot as plt

def data_with_selenium(url):
    s = Service("C:\\Users\\liz\\PycharmProjects\\pythonProject3\\driver\\chromedriver.exe")
    try:
        driver = webdriver.Chrome(service=s)
        driver.get(url=url)
        #time.sleep(5)

        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    with open("index_selenium.html", encoding="utf-8") as file:
        scr = file.read()

    soup = BeautifulSoup(scr, "lxml")
    names = soup.find_all("table", class_="Item__container--24M")
    names_all = []
    for name in names:
        name = name.find("a")
        names_all.append(name.string.strip())

    names_all1 = []
    for name1 in names:
        name1 = name1.find_all("td")[2]
        name1 = name1.text
        name1 = name1.replace("%","")
        name1 = name1.replace(",", ".")
        name1 = float(name1)
        names_all1.append(name1)

    data = {"company": names_all,
            "count_in_%": names_all1}
    table = pd.DataFrame(data)

    plus = table[table["count_in_%"]>=0]
    minus = table[table["count_in_%"] < 0]

    #print("Лидеры роста")
    #print(plus)
    #print("Лидеры падения")
    #print(minus)

    x_p = plus["company"]
    y_p = plus["count_in_%"]
    plt.figure(figsize=(13, 6))
    plt.title('Лидеры роста')
    plt.plot(x_p, y_p)
    plt.grid()
    plt.xlabel("Компании")
    plt.ylabel("Значение в процентах")

    x_m = minus["company"]
    y_m = minus["count_in_%"]
    plt.figure(figsize=(13, 6))
    plt.title('Лидеры падения')
    plt.plot(x_m, y_m)
    plt.grid()
    plt.xlabel("Компании")
    plt.ylabel("Значение в процентах")

    plt.show()

def main():
    data_with_selenium(url="https://www.finam.ru/")

if __name__ == '__main__':
    main()


