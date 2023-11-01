import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_name(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')) > 0
    time.sleep(15)
