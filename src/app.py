from dotenv import load_dotenv
import sys

from services.open_url_list import OpenURLList
from utils.prompt import UtilPrompt

# Load env variables
load_dotenv()

service_mapping = {
    "open_url_list": OpenURLList()
}

# Service definition
prompt = UtilPrompt()

if len(sys.argv) > 1:
    view = sys.argv[1] in service_mapping.keys()
    if sys.argv[1] in service_mapping.keys():
        service_mapping[sys.argv[1]].run()
    else:
        prompt.message("Option not found, please choose one of the next services:\n"+"\n".join(service_mapping.keys()))
else:
    prompt.message("Option not found, please choose one of the next services:\n"+"\n".join(service_mapping.keys()))
