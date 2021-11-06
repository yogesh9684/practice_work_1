from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL= driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@name='proceed']").click()

alert = driver.switch_to_alert()
print(alert.text)
time.sleep(2)
#alert.accept()
alert.dismiss()
