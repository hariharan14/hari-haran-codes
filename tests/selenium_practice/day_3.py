import time

from grpc import services
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service



# if no permission use below service class, or else go for the above
# service_obj = Service('D:\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)
# driver.get("http://www.python.org")


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
driver.get("http://www.python.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)




time.sleep(2)