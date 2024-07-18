from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.welcome_csselector = ".oxd-userdropdown"
        self.logout_link_linkText = "Logout"
        
    def click_welcome(self):
        self.driver.find_element(By.CSS_SELECTOR, self.welcome_csselector).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()
