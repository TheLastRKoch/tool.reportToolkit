from dotenv import load_dotenv
import sys

from services.clone_repos import ServiceCloneRepositories
from services.open_url_list import ServiceOpenURLList
from services.get_licenses import ServiceGetLicenses
from services.check_url_list import ServiceCheckURLList
from utils.prompt import UtilPrompt

# Load env variables
load_dotenv()

service_mapping = {
    "check_url_list": ServiceCheckURLList(),
    "open_url_list": ServiceOpenURLList(),
    "clone_repos": ServiceCloneRepositories(),
    "get_licenses": ServiceGetLicenses(),
}

# Service definition
prompt = UtilPrompt()

if len(sys.argv) > 1:
    sys.argv[1] in service_mapping.keys()
    if sys.argv[1] in service_mapping.keys():
        service_mapping[sys.argv[1]].run()
    else:
        prompt.message("Option not found, please choose one of the next services:\n"+"\n".join(service_mapping.keys()))
else:
    prompt.message("Option not found, please choose one of the next services:\n"+"\n".join(service_mapping.keys()))
