import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


# using service if we cant access the drivers directly due to firewall or vpn
# if no permission use below service class, or else go for the above
# service_obj = Service('D:\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)
# driver.get("http://www.python.org")

# Opening a window, maximizing
# driver = webdriver.Chrome()
# # driver = webdriver.Firefox()
# # driver = webdriver.Edge()
# driver.get("http://www.python.org")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

# # filling a form
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice")
# driver.maximize_window()
# # enter name, email, and pass
# # driver.find_element(By.NAME, "name").send_keys("Hari")
# # CSS -
# # (By.CSS_SELECTOR, 'tagname[attribute="value"]') or
# # (By.CSS_SELECTOR, '#id') or
# # (By.CSS_SELECTOR, '.class')
# driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys("Hari")
# driver.find_element(By.NAME, "email").send_keys("helo@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
# # checkbox
# driver.find_element(By.ID, "exampleCheck1").click()
# # radio button with types of css
# # driver.find_element(By.CSS_SELECTOR, 'input[value="option2"]').click()
# driver.find_element(By.CSS_SELECTOR, '#inlineRadio2').click()
# # XPATH - '//tagname[@attribute="value"]'
# driver.find_element(By.XPATH, '//input[@type="submit"]').click()
# # XPATH having same type=text, but referring through the index
# driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys('Good')
# msg = driver.find_element(By.CLASS_NAME, "alert-success").text
# # print(msg)
# #
# # assert "Success" in msg
# driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()


# ----------------------------------------------------------------------------------------
# # changing password
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/client")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys("Hello@123")
# driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys("Hello@123")
# # driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


# ----------------------------------------------------------------------------------------
# static dropdown
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice")
# driver.maximize_window()
# dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
# dropdown.select_by_visible_text('Female')
# time.sleep(2)
# dropdown.select_by_index(0)


# ----------------------------------------------------------------------------------------
# # dynamic dropdowns
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/dropdownsPractise")
# driver.maximize_window()
#
# time.sleep(2)
# driver.find_element(By.ID, 'autosuggest').send_keys('Ind')
# time.sleep(2)
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
# time.sleep(2)
# print(len(countries))
# for country in countries:
#     if country.text == 'India':
#         country.click()
#         break
# time.sleep(2)
# assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

# ----------------------------------------------------------------------------------------
# Checkbox
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()
# check = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# time.sleep(2)
# print(len(check))
# for box in check:
#     if box.get_attribute('value') == 'option2':
#         box.click()
#         assert box.is_selected()
#         break
# or simply we can, the above is to show
# driver.find_element(By.ID, "checkBoxOption2").click()

#radio
# radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
# time.sleep(2)
# print(len(radio))
# for but in radio:
#     if but.get_attribute('value') == 'radio1':
#         but.click()
#         assert but.is_selected()
#         break
# or
# radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# time.sleep(2)
# radio[2].click()
# time.sleep(2)
# assert radio[1].is_selected() # fails

# verifying whether the text box is displayed
# assert driver.find_element(By.ID, 'displayed-text').is_displayed()
# driver.find_element(By.ID, 'hide-textbox').click()
# time.sleep(2)
# assert not driver.find_element(By.ID, 'displayed-text').is_displayed()

# verifying java pop ups
name = 'Hari'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

alert = driver.switch_to.alert
alertxt = alert.text
print(alertxt)
assert name in alertxt
alert.accept()


time.sleep(2)