from services.service_logger import ServiceLogger as log
from services.service_command import ServiceCommand
from services.service_request import ServiceRequest
from utils import Utils
from urllib import parse
import jmespath
import json
import re


INPUT_FILE_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/components.xlsx"
PACKAGE_MANAGER_MAPPING = {"gem":{"name":"Ruby Gems","url":"https://rubygems.org/api/v1/gems/{package_name}.json?version={version}","pattern":"licenses | join('& ',@)"},"npm":{"name":"JavaScript NPM","url":"https://registry.npmjs.org/{package_name}/{version}","pattern":"license"},"pypi":{"name":"Python Pypi","url":"https://pypi.org/pypi/{package_name}/{version}/json","pattern":"info.license"},"golang":{"name":"Golang pkg","url":"https://api.deps.dev/v3alpha/systems/go/packages/{package_name}/versions/{version}","pattern":"licenses | join('& ',@)"}}
PATTERN_GET_KEYWORD = r"pkg:(.+?)\/"
CMD_OPEN_FILE = "open {path}"


def get_license(url, pattern):
    # Request

    # Init services
    service_request = ServiceRequest()

    r = service_request.get(url=url)
    if r.status_code // 10 != 20:
        # log an error
        return "N/A"
    json_body = json.loads(r.text)
    query = jmespath.compile(pattern)
    return query.search(json_body)


if __name__ == "__main__":

    # Init services
    service_command = ServiceCommand()

    # Open input file
    service_command.background(CMD_OPEN_FILE.format(path=INPUT_FILE_PATH))
    service_command.clear()
    input("Please press any key to continue\n")
    service_command.clear()
    log.info("Process started")

    # Open CSV
    csv_file = Utils.read_xlsx(INPUT_FILE_PATH)

    # For each row in the CSV
    for row in csv_file:
        try:
            log.info(f"Start procesing {row['Organization']} {row['Repository']} {row['Name']}")
            # Identify the type of package
            purl = row["Purl"]
            keyword = re.search(PATTERN_GET_KEYWORD, purl).group(1)

            package_name = row["Name"]
            package_version = row["Version"]

            if (keyword == "golang"):
                package_name = parse.quote(package_name, safe="")

            url = PACKAGE_MANAGER_MAPPING[keyword]["url"].format(
                package_name=package_name,
                version=package_version
            )
            name = PACKAGE_MANAGER_MAPPING[keyword]["name"]
            pattern = PACKAGE_MANAGER_MAPPING[keyword]["pattern"]
            log.trace("Found package manager "+name)
            license = get_license(url, pattern)
            if license == "":
                license = "N/A"
        except Exception as ex:
            log.error("Someting went wrong during the license fetching process")
            log.error(ex)
            license = "N/A"
        finally:
            row["Licenses"] = license
            log.info(f"End procesing {row['Organization']} {row['Repository']} {row['Name']}")

    Utils.write_xlsx(csv_file, INPUT_FILE_PATH)
    service_command.background(CMD_OPEN_FILE.format(path=INPUT_FILE_PATH))
    log.info("Process finished")
