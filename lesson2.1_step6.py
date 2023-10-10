from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x_element_check = x_element.get_attribute("valuex")
    x = x_element_check
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
