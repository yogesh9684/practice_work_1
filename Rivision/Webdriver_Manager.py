from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

import time

Browser_Name = "Opera"

if Browser_Name=="Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
elif Browser_Name == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif Browser_Name ==  "Safari":
        driver = webdriver.Safari()
elif Browser_Name == "Opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    print("Please Enter Correct Browser Name" +  Browser_Name)
    raise Exception ("Driver Not Found " )

driver.implicitly_wait(5)

driver.get("https://stagingmoxie.xyz/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("yogesh+s@moxie.xyz")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("pepo12345")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

print(driver.title)

driver.quit()




