from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("https://web.remonline.app/login")

    login_box = driver.find_element(By.NAME, "login")
    login_pass = driver.find_element(By.NAME, "password")

    login_box.send_keys("vasily.dmitriev")
    login_pass.send_keys("vasily.dmitriev")

    driver.find_element(By.CLASS_NAME, "b-btn").click()

    sleep(1)
    #после логина должна прогрузиться страница админки
    #явное ожидание загрузки меню bt_css_selector("[href='/staff/companies']")
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/staff/companies']"))
    )
    button.click()

    #driver.get('https://web.remonline.app/staff/companies/')
    #ждем прогрузи страниці с компаниями
    sleep(1)
    button = WebDriverWait(driver, 15).until(
        EC.visibility_of(driver.find_element(By.XPATH, "//div[@data-cid='table-body-row']"))
    )


# //div[@data-cid='table-body-row']/div[1]
#tariffs = driver.find_elements_by_class_name("iQ5WK")

#set up table filter parameters

    driver.find_element(By.CLASS_NAME, value="js-tariffs-filter").click()
    butt = driver.find_elements(By.XPATH, value="//*[@data-cid='search-checked-dp']")

    n = len(butt)
    print('нашел ', n, ' buttons')
    if n > 0:
        for i in range(n-3):
            butt[i].click()

    driver.find_element_by_xpath("//body").click()

except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)

sleep(10)

#need clic on <div class="js-date-selector" data-validation-position="absolute" name="grace_till">  xpass //div[@class="js-date-selector"]
#click on xpath //div[@class="js-selector-item" and @data-type="CUSTOM"]
#find //div[@class="b-in-holder"]/input
# send keys = 21.04.2022 0000:0404 to 24.04.2122 2323:0404  , click()
# потом клик рядом

# print table by line
try:
    table_lines = driver.find_elements(By.XPATH, value="//div[@data-cid='table-body-row']")

    for i in table_lines:
        s = i.text
        s = s.replace('\n',';')
        print(s)
except:
    print('не нашел строки')
finally:
    print('отработал')

sleep(1)
driver.close()