from services.service_template import ServiceTemplate
from utils.variable import get_and_check_variables
from utils.filter import UtilJMESpath
from utils.prompt import UtilPrompt
from utils.file import UtilFile
import json

env = get_and_check_variables(["FILE_PATH", "JMESPAHT_QUERY"])


class ServiceGetCalEvents(ServiceTemplate):
    """
    This method calculates the duration of the events in the calendar,
    it removes the EndDate key as the AI model do not currently support it
    """

    def calculate_duration(self, json_formatted):
        for event in json_formatted:
            start_date = event["StartDate"]
            end_date = event["EndDate"]
            duration = end_date - start_date
            event["Duration"] = duration
            event.pop("EndDate")
        return json

    def run(self):

        # Define utils
        prompt = UtilPrompt()
        util_file = UtilFile()
        jmespath = UtilJMESpath()

        prompt.welcome("Get Calendar Events")
        util_file.open(env["FILE_PATH"])
        prompt.wait("Please enter the json calendar file\n")
        json_file = json.loads(util_file.read_text_file(env["FILE_PATH"]))
        json_formatted = jmespath.filter(env["JMESPAHT_QUERY"], json_file)
        event_list = self.calculate_duration(json_formatted)
        util_file.write_text_file(env["FILE_PATH"], json.dumps(event_list))
        util_file.open(env["FILE_PATH"])
