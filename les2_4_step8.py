from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(1)
#ждем не менее 15 сек, пока на цена не дойдет до 100$

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='price']"), '$100')
    )
    browser.find_element_by_css_selector("button.btn").click()

    x = browser.find_element_by_css_selector("[id='input_value']").text

    y_val = str(calc(x))

    browser.find_element_by_css_selector("[id='answer']").send_keys(y_val)

    browser.find_element_by_css_selector("[id='solve']").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
