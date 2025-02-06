from os import environ as env
from flask import Flask
import json

from utils.file import UtilFile


class ServiceMockAPI:
    def handler(self, response: dict, status_code):
        return response, status_code

    def run(self):

        # Utils definition
        util_file = UtilFile()

        route_list_path = env["ROUTE_LIST_PATH"]
        route_list = json.loads(util_file.read_text_file(route_list_path))

        if route_list is None or len(route_list) > 0:
            app = Flask(__name__)

            for route in route_list:
                path = route.get("path")
                response = route.get("response")
                status_code = route.get("status_code")
                app.add_url_rule(path, view_func=lambda: self.handler(response, status_code))
                print(f"{path} configured")

            app.run(debug=True)
        else:
            print("Error: Could not load the configured endpoints.")


if __name__ == "__main__":
    service_mock_api = ServiceMockAPI()
    service_mock_api.run()
