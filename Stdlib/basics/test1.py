from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

userstr = "viperll007"
passstr = "swakshwar###1234"
your_gmail="ghoshswakshwar06@gmail.com"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

steam = driver.get("https://store.steampowered.com")
link = driver.find_element_by_link_text("login")
link.click()

username = driver.find_element_by_id("input_username")
username.send_keys(userstr)

password = driver.find_element_by_id("input_password")
password.send_keys(passstr)

sign = driver.find_element_by_tag_name("button")
sign.click()


