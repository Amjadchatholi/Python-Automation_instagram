# 1
from selenium import webdriver
from config import USERNAME, PASSWORD
import time

users = ['mhmd_nashif06','nish.aj._', '__16_diary']

browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')

browser.maximize_window()

browser.get('https://www.instagram.com/')

time.sleep(2)

user_field=browser.find_element_by_name('username')
user_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]') 
login_btn.click()

time.sleep(3)



for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    time.sleep(4)

# 2
# from selenium import webdriver
# import time
# from config import USERNAME, PASSWORD


# browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')
# browser.get('https://www.instagram.com/')
# time.sleep(2)

# Username=browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
# Username.send_keys(USERNAME)
# time.sleep(2)

# Password= browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
# Password.send_keys(PASSWORD)
# Password.submit()
# time.sleep(2)


# # Notnow = browser.find_element_by_css_selector('button[type="button"]') 
# # Notnow.click()

# Notnow = browser.find_element_by_xpath('//*[@id="mount_0_0_wi"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
# Notnow.click()
# time.sleep(2)


# Unow=browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
# Unow.click()
# time.sleep(3)

# def firstpic():
#     time.sleep(2)
#     picorved=browser.find_element_by_class_name("_aakl")
#     picorved.click()

# def likepic():
#     time.sleep(4)    
#     like=browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/section/div/div[3]/div[1]/div/article[1]/div/div[3]/div/div/section[1]/span[1]/button")
#     like.click()

# firstpic()
# likepic()    










    

