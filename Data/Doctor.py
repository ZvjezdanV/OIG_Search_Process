
import datetime

class Doctor:
    """This is our base class for our doctor's information"""
    
    firstName = ""
    lastName = ""
    hasExclusions = False
    numberOfExclusions = 0
    searchDate = ""
    
    
    def __init__(self, first_name: str, last_name: str):
        self.firstName = first_name
        self.lastName = last_name
        self.searchDate = str(datetime.datetime.now())
        
    def set_doctor_exclusions(self, has_exclusions: bool, number_of_exclusions: int):
        self.hasExclusions = has_exclusions
        self.numberOfExclusions = number_of_exclusions
                