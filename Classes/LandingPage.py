
from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver
from selenium.webdriver.common.by import By
from Data.Doctor import Doctor
from Classes.SearchResultsPage import SearchResultsPage


class LandingPage(WebDriver):
    """This is the landing page that's associated to our OIG Site"""
    
    def __init__(self, object: Optional[ChromeWebDriver]):
        if object != None:
            self.chrome_driver = object
            self.__verify_page_load()
        else:
            self.chrome_driver = WebDriver().chrome_driver
            self.chrome_driver.get("https://exclusions.oig.hhs.gov/")
            self.__verify_page_load()
    
                
    # Private Method           
    def __verify_page_load(self):
        self.wait_displayed("//h1[contains(text(), 'Exclusions Database')]")
        self.wait_displayed("//input[contains(@name, 'FirstName')]")
        self.wait_displayed("//input[contains(@name, 'LastName')]")
        self.wait_displayed("//input[contains(@name, 'SearchSP')]")
        
    
    # Private Method
    def __enter_first_name(self, doctor: Doctor):
        self.chrome_driver.find_element(By.XPATH, "//input[contains(@name, 'FirstName')]").send_keys(doctor.firstName)
        
     
     # Private Method   
    def __enter_last_name(self, doctor: Doctor):
        self.chrome_driver.find_element(By.XPATH, "//input[contains(@name, 'LastName')]").send_keys(doctor.lastName)
        
        
    # Private Method
    def __click_search(self):
        for i in range(5):
            self.chrome_driver.find_element(By.XPATH, "//input[contains(@name, 'SearchSP')]").click()
            if self.is_displayed("//h1[contains(., 'Search Results')]"):
                break
            elif i == 4:
                raise Exception('Failed to conduct the Search for our Doctor in our Landing Page.')
        return SearchResultsPage(self.chrome_driver)
        
            
    def search_for_doctor(self, doctor: Doctor):
        self.__enter_first_name(doctor)
        self.__enter_last_name(doctor)
        return self.__click_search()