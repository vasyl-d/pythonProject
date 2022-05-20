from selenium import webdriver
import time
import math

find_st = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"

value1 ='input'
value2 ='last_name'
value3 ='city'
value4 ='country'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_st = browser.find_element_by_link_text(find_st)
    input_st.click()


    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла