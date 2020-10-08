
from Classes.ExclusionResultsDetailsPage import ExclusionResultsDetailsPage
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver
from selenium.webdriver.common.by import By


class SearchResultsPage(WebDriver):
    """This is the Results Page after we conduct our initial search"""
    
    doExclusionsDisplay = False
    numberOfExclusions = 0
    searchConductedDate = ""
    sourceDataUpdatedDate = ""
    
    
    def __init__(self, object: ChromeWebDriver):
        self.chrome_driver = object
        self.__verify_page_load()
        self.doExclusionsDisplay = self.__do_exclusion_records_display()
        self.numberOfExclusions = self.__get_number_of_exclusion_records()
        self.searchConductedDate = self.__get_search_conducted_date()
        self.sourceDataUpdatedDate = self.__get_source_data_updated_date()
        
        
    # Private Method
    def __verify_page_load(self):
        self.wait_displayed("//h1[contains(., 'Search Results:') and contains(., 'Individuals')]")
        self.wait_displayed("//a[contains(@id, 'BackToSearch') and text()='Return to Search']")
        
        
    # Private Method
    def __do_exclusion_records_display(self):
        number = self.chrome_driver.find_elements(By.XPATH, "//table[@class='leie_search_results']//tbody//tr").__len__()
        return True if number > 1 else False
    
    
    # Private Method
    def __get_number_of_exclusion_records(self):
        number = self.chrome_driver.find_elements(By.XPATH, "//table[@class='leie_search_results']//tbody//tr").__len__()
        return number - 1 if number > 1 else 0
    
    
    # Private Method
    def __get_search_conducted_date(self):
        temp = self.chrome_driver.find_element(By.XPATH, "//div[@class='timeStampResults']//p").text
        temp = str(temp.split("Source data updated")[0])
        return temp[0:temp.find("on OIG")].replace("Search conducted", "").strip() 
    
    
    # Private Method
    def __get_source_data_updated_date(self):
        temp = self.chrome_driver.find_element(By.XPATH, "//div[@class='timeStampResults']//p").text
        return str(temp.split("Source data updated")[1]).replace("on", "").strip() 
    
    
    # Private Method
    def __open_exclusion_record(self, xpath: str):
        for i in range(5):
            self.chrome_driver.find_element(By.XPATH, f'{xpath}').click()
            if self.is_displayed("//h1[contains(., 'Results: Verify')]"):
                break
            elif i == 4:
                raise Exception(f'Failed to find XPATH: {xpath}')
        return ExclusionResultsDetailsPage(self.chrome_driver)
    
    
    def get_exclusion_records(self):
        doctorExclusionRecords = []
        for i in range(1, self.numberOfExclusions + 1):
            exclusionResultsPage = self.__open_exclusion_record("//table[@class='leie_search_results']//tbody//tr[{0}]//a[text()='Verify']".format(i + 1))
            record = exclusionResultsPage.scrape_details()
            doctorExclusionRecords.append(record.__dict__)
            self = exclusionResultsPage.click_back_to_search()
        return doctorExclusionRecords