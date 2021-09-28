import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get('http://uitestingplayground.com/')
titre = driver.title
print("Le titre de la page est : ", titre)
print("La longueur du titre est: ", len(titre))
driver.back()
driver.forward()
time.sleep(2)
driver.refresh()
driver.close()