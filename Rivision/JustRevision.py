from selenium import webdriver
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/Yogesh/PycharmProjects/JustForRevision/chromedriver')
driver.get("https://www.google.com")
print(driver.title)

driver.implicitly_wait(10)

driver.find_element_by_name("q").send_keys("Dhole Patil College")
time.sleep(3)
element_list = driver.find_elements_by_css_selector('ul.G43f7e li')
print(len(element_list))

for ele in element_list:
    print(ele.text)
    if ele.text == "dhole patil college of engineering logo":
        ele.click()
        break

time.sleep(5)
driver.quit()

