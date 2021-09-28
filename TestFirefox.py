from selenium import webdriver
print("Starting execution on Firefox")
driver = webdriver.Firefox(executable_path="D:\webdriver\geckodriver.exe")
driver.get("https://www.google.tn/")
print("Execution finished with success")