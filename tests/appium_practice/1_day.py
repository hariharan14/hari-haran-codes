import os.path
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# this is failing, so using options
# device_cap = {
#   "automationName": "UiAutomator2",
#   "platformName": "Android",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.google.android.calendar",
#   "appActivity": "com.android.calendar.LaunchActivity"
# }
#
# driver = webdriver.Remote("http://127.0.0.1:4723", device_cap)


# to launch calendar app
# options = UiAutomator2Options()
# options.platform_name = "Android"
# options.automation_name = "UiAutomator2"
# options.device_name = "emulator-5554"
# options.app_package = "com.google.android.calendar"
# options.app_activity = "com.android.calendar.LaunchActivity"
#
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


# to install and launch contact manager
# options = UiAutomator2Options()
# options.platform_name = "Android"
# options.automation_name = "UiAutomator2"
# options.device_name = "emulator-5554"
# options.app_package = "com.example.android.contactmanager"
# options.app_activity = "com.example.android.contactmanager.ContactManager"
# options.app = os.path.abspath("./ContactManager.apk")
#
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# to launch contact manager and add a contact - the app needs update and there is no exe
# options = UiAutomator2Options()
# options.platform_name = "Android"
# options.automation_name = "UiAutomator2"
# options.device_name = "emulator-5554"
# options.app_package = "com.example.android.contactmanager"
# options.app_activity = "com.example.android.contactmanager.ContactManager"
#
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#
# continue_button = driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/continue_button')
# continue_button.click()
#
# ok_button = driver.find_element(AppiumBy.ID, 'android:id/button1')
# ok_button.click()
#
# add_contact = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add Contact')
# add_contact.click()
#
# contact_name = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'com.example.android.contactmanager:id/contactNameEditText')
# contact_name.send_keys('hari')


# using xpath to navigate thru selenium-test-app
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"
options.app_package = "io.selendroid.testapp"
options.app_activity = "io.selendroid.testapp.HomeScreenActivity"
options.app = os.path.abspath("./selendroid-test-app.apk")

# providing the server ip of appium with port 4723 which is common for all the machines
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# clicking using ID
driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/continue_button').click()
time.sleep(2)

# clicking using ID
driver.find_element(AppiumBy.ID, 'android:id/button1').click()

# clicking using XPATH
# driver.find_element(AppiumBy.XPATH, '//tag_element[@attribute="value"]')
# here the attribute can be resource-id, content-desc, text and the corres value of it
# tag_name is the class
driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="startUserRegistrationCD"]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="io.selendroid.testapp:id/input_preferedProgrammingLanguage"]').click()
time.sleep(2)

# dropdown opened, and getting the options details in a list
l = driver.find_elements(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource_id="android:id/text1"]')
time.sleep(2)
print(len(l)) # 8 - dropdown options
for e in l:
    if e.text == "Python":
        e.click()
        break
