from services.service_files import ServiceFiles


EXCLUSIONS = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/exclusions.txt"

service_files = ServiceFiles()
service_files.clean_textfile(EXCLUSIONS)
