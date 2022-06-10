from selenium import webdriver
import time
import pytest


wel_mess = "Congratulations! You have successfully registered!"

#fixture for running browser only 1 time when test class starts and close him after all test

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


def op_link(link, browser):
        welcome_text = ''
        try:
            value = ['.first_block > .form-group > .first',
                     '.first_block > .form-group > .second',
                     '.first_block > .form-group > .third']

#            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            for vl in value:
                element = browser.find_element_by_css_selector(vl)
                element.send_keys("Ответ")

            # Отправляем заполненную форму
            browser.find_element_by_css_selector("button.btn").click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text = browser.find_element_by_tag_name("h1").text
            # записываем в переменную welcome_text текст из элемента welcome_text_elt

        except Exception as ex:
            welcome_text = f"An exception of type {type(ex).__name__} occurred."

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            # browser.quit()
        return welcome_text

class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.parametrize('page', ["registration1.html", "registration2.html"])
    def test_link1(self, browser, page):
        print("start test link: ", page)
        link = f"http://suninjuly.github.io/{page}"
        mess = op_link(link, browser)
        assert mess == wel_mess, mess

    @pytest.mark.regression
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_link2(self, browser):
        print("start test link2")
        link = "http://suninjuly.github.io/registration2.html"
        mess = op_link(link, browser)
        assert mess == wel_mess, mess
