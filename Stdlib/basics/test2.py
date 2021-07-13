from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

userstr = "viperll007"
passstr = "swakshwar###1234"
skin_name = "redline"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

steam = driver.get("https://steamcommunity.com/market")
link = driver.find_element_by_link_text("login")
link.click()

username = driver.find_element_by_id("input_username")
username.send_keys(userstr)

password = driver.find_element_by_id("input_password")
password.send_keys(passstr)

sign = driver.find_element_by_tag_name("button")
sign.click()

sleep(10)

search = driver.find_element_by_id("findItemsSearchBox")
search.send_keys(skin_name)

srchbtn = driver.find_element_by_id("findItemsSearchSubmit")
srchbtn.click()