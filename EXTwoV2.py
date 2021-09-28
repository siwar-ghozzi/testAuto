from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get('https://www.google.tn/')
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_class_name("gN089b").submit()