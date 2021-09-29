from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get('https://nxtgenaiacademy.com/demo-site/')
driver.find_element_by_id("vfb-5").send_keys("Siwar")
driver.find_element_by_id("vfb-7").send_keys("Ghozzi")
driver.find_element_by_xpath(" //input[@id='vfb-8-1']").click()
city = Select(driver.find_element_by_id("vfb-13-country"))
city.select_by_visible_text("Austria")
driver.find_element_by_id("vfb-14").send_keys("ghz@gmail.com")
driver.find_element_by_id("vfb-18").send_keys("08/08/2021")

hour = Select(driver.find_element_by_id("vfb-16-hour"))
hour.select_by_visible_text("07")

minute = Select(driver.find_element_by_id("vfb-16-min"))
minute.select_by_visible_text("15")

ampm = Select(driver.find_element_by_id("vfb-16-ampm"))
ampm.select_by_visible_text("AM")

driver.find_element_by_id("vfb-20-0").click()
driver.find_element_by_id("vfb-3").send_keys("01")
driver.find_element_by_id("vfb-4").click()