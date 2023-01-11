from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


URL_1 = "https://www.amazon.com/Logitech-Master-Wireless-Mouse-Rechargeable/dp/B071YZJ1G1/ref=sr_1_13?crid" \
      "=1CC3BNZCI48TE&keywords=logitech%2Bmouse&qid=1673442393&s=electronics&sprefix=logitech%2Bmous%2Celectronics" \
      "-intl-ship%2C223&sr=1-13&th=1 "

URL_2 = "https://www.python.org/"

chrome_driver_path = "C:/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL_2)

# web scrapping using selenium

# price = driver.find_element(by="id", value="corePrice_feature_div")
# print(price.tag_name)
# print(price.text)

# logo = driver.find_element(by="name", value="q")
# print(logo.tag_name)

# element = driver.find_element(by="css selector", value=".documentation-widget p a")
# print(element.text)

# link = driver.find_element(by="xpath", value="//*[@id='container']/li[8]/ul/li[1]/a")
# print(link.get_property("href"))

# driver.find_elements()

if input() == "1":
    driver.close()


