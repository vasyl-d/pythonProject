from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    selector = ["[id='treasure']",
        "[id='answer']",
        "[id='robotCheckbox']",
        "[id='robotsRule']"]


    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector(selector[0])
    x = x_element.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_css_selector(selector[1])
    answer.send_keys(str(y))

    for i in [2,3]:
        el = browser.find_element_by_css_selector(selector[i])
        el.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()