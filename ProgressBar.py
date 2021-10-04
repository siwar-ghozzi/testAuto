from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get('http://www.uitestingplayground.com/')
driver.maximize_window()
driver.find_element_by_xpath("//a[@href='/progressbar']").click()

driver.find_element_by_id("startButton").click()
val_pb = driver.find_element_by_id("progressBar").text
while val_pb != "75%":
    val_pb = driver.find_element_by_id("progressBar").text
driver.find_element_by_id("stopButton").click()
print(driver.find_element_by_id("result").text)
driver.quit()

