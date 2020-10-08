
import sys
import json
import datetime
from Functions.FolderCreation import FolderCreation
from Functions.FileCreation import FileCreation
from Classes.LandingPage import LandingPage
from Data.Doctor import Doctor

if len(sys.argv) != 3:
    raise Exception("OIG_Search_Process: Format Error! Proper format not provided. Please follow the below format:\n{0} {1} {2} {3}"
                    .format("python", "file_path_to_main_program.py", "doctor_first_name", "doctor_last_name"))


doctor = Doctor(first_name = sys.argv[1], last_name = sys.argv[2])

# Create our folder and files
folder_path = FolderCreation.create_folder("OIG_Search_Results_Folder")
file_name = "{0}{1}_{2}.txt".format(doctor.firstName, doctor.lastName, f'{datetime.date.today().month}{datetime.date.today().day}{datetime.date.today().year}')
file_path = FileCreation.create_textfile(folder_path = folder_path, file_name = file_name)

# Open our OIG site and search for our doctor
landingPage = LandingPage(None)
searchResultsPage = landingPage.search_for_doctor(doctor)

# Populate our found data to our doctor record
doctor.set_doctor_exclusions(has_exclusions = searchResultsPage.doExclusionsDisplay,
                             number_of_exclusions = searchResultsPage.numberOfExclusions)

doctor_exclusions_json = searchResultsPage.get_exclusion_records() if searchResultsPage.doExclusionsDisplay else ""

# Open our file and populate it with our doctor's data
file = open(file_path, "w")
file.write(f'Doctor: {doctor.firstName} {doctor.lastName}\n')
file.write(f'{json.dumps(doctor.__dict__, indent = 4)}\n')

if doctor.hasExclusions:
    file.write('Exclusions:\n')
    for i in range(doctor_exclusions_json.__len__()):
        file.write(f'{json.dumps(doctor_exclusions_json[i], indent = 4)}\n')

file.flush()
file.close()

searchResultsPage.chrome_driver.quit()
searchResultsPage.chrome_driver.stop_client()

# Update our console so our user knows that this process completed successfully
print(f'Updated: {file_path} with Doctor Data ( {doctor.firstName} {doctor.lastName} ) successfully.')