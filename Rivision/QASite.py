# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# # # For_Firefox
# # # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/automation-practice-form")
#
# driver.maximize_window()
#
#
# driver.find_element(By.ID,'firstName').send_keys('Yogesh')
# driver.find_element(By.ID,'lastName').send_keys('Sawant')
# driver.find_element(By.ID,'userEmail').send_keys('yogesh50008@gmail.com')
# driver.find_element(By.XPATH,"//label[@for='gender-radio-1']").click()
# driver.find_element(By.ID,'userNumber').send_keys('9011743126')
# driver.find_element(By.ID,'dateOfBirthInput').click()
# calender = driver.find_element(By.CLASS_NAME,'react-datepicker__month-select').click()
# month= driver.find_element(By.CLASS_NAME,'react-datepicker__month-select')
# select = Select(month)
# select.select_by_visible_text('December')
# driver.find_element(By.XPATH,"//div[@class='react-datepicker__month']/div[@class='react-datepicker__week'][3]/div[@class='react-datepicker__day react-datepicker__day--014']").click()
# driver.find_element(By.ID,"subjectsInput").send_keys('How are you ?')
#
# #          <<< To Select the Multiple Value by Generic method >>>
#
#
# def select_multiple_hobbies(OptionsList,value):
#     if not value[0] == 'all':
#         for ele in check_box:
#             print(ele.text)
#             for k in range(len(value)):
#                 if ele.text == value[k]:
#                     ele.click()
#                     break
#     else:
#         try:
#             for ele in OptionsList:
#                 ele.click()
#         except Exception as e:
#                 print(e)
#
#
#
# check_box = driver.find_elements(By.CSS_SELECTOR,'#hobbiesWrapper label.custom-control-label')
# value_list = ['Sports','Reading','Music']
# #value_list=['all']
# select_multiple_hobbies(check_box,value_list)
#
# #              <<< Select the Value with Multiple checkbox >>>
#
# # driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-1']").click()
# # driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-2']").click()
# # driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-3']").click()
#
#
#
# upload_picture = driver.find_element(By.ID,'uploadPicture').send_keys("/Users/Yogesh/Downloads/yogeshsawant.jpg")
# driver.find_element(By.ID,'currentAddress').send_keys('Driver [/Users/Yogesh/.wdm/drivers/chromedriver/mac64/95.0.4638.17/chromedriver] found in cache')
# time.sleep(5)
# driver.find_element(By.ID,'state').click()
# time.sleep(30)
# driver.find_element(By.XPATH,"//div[@id='state']//div[@class=' css-yk16xz-control']/div[@class=' css-1hwfws3']").click()
#


# class ParentClass:
#     def par_func(self):
#          print("I am parent class function")
#
# # Child class
# class ChildClass(ParentClass):
#     def child_func(self):
#          print("I am child class function")
#
# # Driver code
# obj1 = ChildClass()
# obj1.par_func()
# obj1.child_func()






# a =int(input('Enter the Number of your choice:'))
# if a > 0:
#     for y in range(2,a):
#         if (a % 2) == 0:
#             print(a , 'is not prime Number ')
#             break
#         else:
#             print(a, 'is a prime Number ')
#             break
#
#



# List1 = [1,2,3,4,5,1,3,2,1,4,5,4]
# List2=[]
# for r in List1:
#     if r not in List2:
#         List2.append(r)
#     else:
#         print(r,end='')
#
#
# l=[1,2,3,4,5,2,3,4,7,9,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i,end=' ')



