from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3406618637&" \
      "f_AL=true&keywords=software%20engineer&refresh=true"

USERNAME = ""
PASSWORD = ""

chrome_driver_path = "C:/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)

time.sleep(1)
# click sign in
sign_in = driver.find_element(by="xpath", value="/html/body/div[3]/header/nav/div/a[2]")
sign_in.click()

time.sleep(1)
# enter username
username = driver.find_element(by="id", value="username")
username.clear()
username.click()
username.send_keys(USERNAME)
time.sleep(1)
# enter password
password = driver.find_element(by="id", value="password")
password.clear()
password.click()
password.send_keys(PASSWORD)
time.sleep(1)
# ENTER
password.send_keys(Keys.RETURN)

# minimize chat
# min_button = driver.find_element(by="id", value="ember129")
# min_button.click()
time.sleep(5)

# jobs_list = driver.find_elements(
jobs_list = driver.find_element(
    by="xpath",
    value="//*[@id='main']/div/section[1]/div/ul/li[1]"
)
# for job in jobs_list:
#     print(job.text)

jobs_list.click()
time.sleep(1)

easy_apply = driver.find_element(by="css selector", value=".jobs-apply-button--top-card button")
easy_apply.click()

time.sleep(1)

next = driver.find_element(by="css selector", value="div.jobs-easy-apply-content button")
next.click()
time.sleep(1)


input()



