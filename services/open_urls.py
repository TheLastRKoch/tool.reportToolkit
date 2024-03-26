from services.service_prompt import ServicePrompt
from utils import Utils
import os

URL_LIST_PATH = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/URLs.txt"
NUM_OF_URL = 15


def open_urls(url_list):
    count = 1
    formatterd_list = list(dict.fromkeys(url_list))
    for idx, url in enumerate(formatterd_list):
        if count == NUM_OF_URL:
            input(f"{idx+1}/{len(formatterd_list)} URLs opened press any key to continue")
            count = 0
        os.system("open "+url)
        count = count+1


def clean_url_list_file():
    os.system(f"echo > {URL_LIST_PATH}")


def open_url_list_file():
    os.popen("open "+URL_LIST_PATH).read


if __name__ == "__main__":
    # Services
    service_prompt = ServicePrompt()

    service_prompt.welcome("Open URLS")
    open_url_list_file()
    service_prompt.wait("Please fill the repository list file")
    url_list = Utils.get_file_items(URL_LIST_PATH)
    service_prompt.message(f"Found {len(url_list)} unique URLs\n")
    open_urls(url_list)
    clean_url_list_file()
    service_prompt.message("\n\nProcess finished successfully")
