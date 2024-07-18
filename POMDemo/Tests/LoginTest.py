from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePages import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):
    
    chrome_options = Options()

    
    @classmethod
    def setUpClass(cls):
        cls.chrome_options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=cls.chrome_options)
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()
        
        #self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #self.driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown").click()
        #time.sleep(3)
        #self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/anoni/OneDrive/Escritorio/Curso_Selenium/Reportes'))