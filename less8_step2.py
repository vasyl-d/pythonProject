from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    selector1 = ["[id='num1']",
        "[id='num2']"]

    selector2 = ["[id='dropdown']",
        "button.btn"]

    y = 0
    browser = webdriver.Chrome()
    browser.get(link)

    for i,el in enumerate(selector1):
        y += int(browser.find_element_by_css_selector(el).text)

    sel_y = f"[value='{y}']"

    browser.find_element_by_css_selector(selector2[0]).click()
    browser.find_element_by_css_selector(sel_y).click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(selector2[1])
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()