#from selenium import webdriver
from selenium.webdriver.common.by import By
from POMDemo.Locator.locators import Locators

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = "password"
        self.login_button_csselector = ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button"
        
    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.NAME, Locators.password_textbox_name).clear()
        self.driver.find_element(By.NAME, Locators.password_textbox_name).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_csselector).click()