# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.support.ui import Select
#
# import time
# import random
#
# #For_Chrome
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# #For_Firefox
# # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
# driver.implicitly_wait(10)
# driver.get("https://stagingmoxie.xyz/login")
#
# driver.maximize_window()
#
# Email = driver.find_element(By.XPATH,"//input[@type='email']")
# Email.send_keys('yogesh+gridview@moxie.xyz')
# Password = driver.find_element(By.XPATH,"//input[@type='password']")
# Password.send_keys('pepo1234')
# Login_Button = driver.find_element(By.XPATH,"//button[@type='submit']")
# Login_Button.click()
#
# time.sleep(5)
#
# Click_on_Add_class = driver.find_element(By.XPATH,"//button[@class='btn btn-primary letter-spacing-1 font-weight-bold jTeamCreateClass jCreateClassBtn']")
# Click_on_Add_class.click()
#
# driver.execute_script("window.scrollTo(0, 700)")
#
# time.sleep(2)
#
# workout_type = driver.find_element(By.XPATH,"//div[@class='filter-option']//div[contains(text(),'Workout Type')]")
# workout_type.click()
#
# #          <<<Create a Generic Method and Select the Value from DropDown >>>
#
# # def select_value_from_dropdown(DropdownOptionList,value):
# #     print(len(DropdownOptionList))
# #     for ele in DropdownOptionList:
# #         print(ele.text)
# #         if ele.text == value:
# #             ele.click()
# #             break
# #
# # List_of_workout = driver.find_elements(By.CSS_SELECTOR,'ul.dropdown-menu li a')
# # select_value_from_dropdown(List_of_workout,'Barre')
#
#
# #     <<< Selecting the Random Value From DropDown >>>
#
# # List_of_workout = driver.find_elements(By.CSS_SELECTOR,'ul.dropdown-menu li a')
# # print(len(List_of_workout))
# # having_list = ['Aerial','Barre','Boxing','Cardio','Cycling','Dance','Flexibility','HIIT','Kids','Martial' 'Arts','Meditation','Pilates','Prenatal','Seniors']
# # choose_choise = random.choice(having_list)
# # for ele in List_of_workout:
# #     if ele.text == choose_choise:
# #         ele.click()
# #         break
#
# #driver.quit()
#
#
l=[1,2,3,4,5,1,3,2,1,4,5,4]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i, end='')




# a=[1,2,3,4,5,1,3,2,1,4,5,4]
# test= sorted(a)
# print(test)
# for i in test:
#     if i is duplicate
#         print(i)



# x = range(0,10)
# for i in x:
#     print(i)
#
#
