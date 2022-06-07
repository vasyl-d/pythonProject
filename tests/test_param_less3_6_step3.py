from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
import pytest


#fixture for running browser only 1 time when test class starts and close him after all test
#fixture moved to conftest.py


def answer():
    return math.log(int(time.time()))


wel_mess = "Correct!"
urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


def op_link(link, browser):
    mess = ''
    try:
        browser.get(link)

        element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area"))
        )
        element.send_keys(str(answer()))

        # Отправляем заполненную форму
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        element.click()

        # Проверяем, что смогли
        element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        mess = element.text

    except Exception as ex:
        mess = f"An exception of type {type(ex).__name__} occurred."

    return mess


class TestMainPage1():

    @pytest.mark.parametrize('page', urls)
    def test_link1(self, browser, page):
        print("start test link: ", page)
        mess = op_link(page, browser)
        assert mess == wel_mess, mess
