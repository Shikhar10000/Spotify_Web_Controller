from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
def login(uname,passw,chromedriver_path):
	driver = webdriver.Chrome(executable_path=chromedriver_path)
	driver.maximize_window()
	url ='https://open.spotify.com/browse/featured'
	driver.get(url)
	element=element = driver.find_element_by_xpath(("//button[contains(text(),'Log in')]"))
	element.click()
	time.sleep(1.5) 
	driver.find_element_by_xpath("//input[@placeholder='Email address or username']").send_keys(uname)
	driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(passw)
	driver.find_element_by_id("login-button").click()
	time.sleep(2)
	return driver
def playlist(name,driver):
	try:
		driver.refresh()
		time.sleep(1.5) 
		driver.find_element_by_xpath(("//span[contains(text(),'"+name.strip()+"')]")).click()
		time.sleep(2) 
		play=driver.find_element_by_xpath("//button[contains(text(),'PLAY')]")
		play.click()
	except:
		driver.refresh()
		time.sleep(1.5) 
		driver.find_element_by_xpath(("//span[contains(text(),'"+name.strip()+"')]")).click()
		time.sleep(2) 
		play=driver.find_element_by_xpath("//button[contains(text(),'PLAY')]")
		play.click()
def closedr(driver):
	driver.close()
	
	
def del_play(driver,name):
	actionChains = ActionChains(driver)
	DEFS= driver.find_element_by_xpath(("//span[contains(text(),'"+name.strip()+"')]"))
	actionChains.context_click(DEFS).perform()
	driver.find_element_by_xpath(("//div[contains(text(),'Delete')]")).click()
	driver.find_element_by_xpath(("//button[contains(text(),'DELETE')]")).click()

