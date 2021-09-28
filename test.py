from selenium import webdriver
print("Starting execution on GOOGLE Chrome")
browser = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
browser.get('https://www.youtube.com/')
browser.close()
print("Execution finished with success")

