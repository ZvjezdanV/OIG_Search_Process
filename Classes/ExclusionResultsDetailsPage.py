
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver
from selenium.webdriver.common.by import By
from Data.DoctorExclusionRecord import DoctorExclusionRecord


class ExclusionResultsDetailsPage(WebDriver):
    """This is our page that houses / displays our Exclusion Details"""
    
    def __init__(self, object: ChromeWebDriver):
        self.chrome_driver = object
        self.__verify_page_load()
        
        
    # Private Method
    def __verify_page_load(self):
        self.wait_displayed("//h1[contains(., 'Results: Verify')]")
        self.wait_displayed("//input[contains(@id, 'btnVerify')]")
        self.wait_displayed("//table[contains(@class, 'verify_info')]")
       
        
    def scrape_details(self):
        doctorExclusionRecord = DoctorExclusionRecord()
        
        doctorExclusionRecord.firstName = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='First Name']/following-sibling::td").text
        
        doctorExclusionRecord.middleName = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Middle Name']/following-sibling::td").text
        
        doctorExclusionRecord.lastName = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Last Name']/following-sibling::td").text
        
        doctorExclusionRecord.dateOfBirth = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[.='DOB']/following-sibling::td").text
        
        doctorExclusionRecord.npi = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='NPI']/following-sibling::td").text
        
        doctorExclusionRecord.upin = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='UPIN']/following-sibling::td").text
        
        doctorExclusionRecord.general = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='General']/following-sibling::td").text
        
        doctorExclusionRecord.specialty = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Specialty']/following-sibling::td").text
        
        doctorExclusionRecord.address = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Address']/following-sibling::td").text
        
        doctorExclusionRecord.address += self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Address']/../following-sibling::tr[1]//td").text
        
        doctorExclusionRecord.exclusionType = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Excl. Type']/following-sibling::td").text
        
        doctorExclusionRecord.exclusionDate = self.chrome_driver.find_element(
            By.XPATH, "//table[contains(@class, 'verify_info')]//th[text()='Excl. Date']/following-sibling::td").text
        
        return doctorExclusionRecord
    
    
    def click_back_to_search(self):
        for i in range(5):
            self.chrome_driver.find_element(By.XPATH, "//a[contains(@id, 'BackToSearch') and contains(text(), 'Return to Search Results')]").click()
            if self.is_displayed("//h1[contains(., 'Search Results:') and contains(., 'Individuals')]"):
                break
            elif i == 4:
                raise Exception('Failed to click "Return to Search Results"')
        from Classes.SearchResultsPage import SearchResultsPage
        return SearchResultsPage(self.chrome_driver)
        