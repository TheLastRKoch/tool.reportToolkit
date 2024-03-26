from services.service_prompt import ServicePrompt
from utils import Utils
import os

# Constants
URL_CLONE_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/cloned"
FILE_WITH_URLS = "/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/repos.txt"


def get_url_parts(url):
    url_part_list = url.split("/")
    return {
        "protocol": url_part_list[0],
        "domain": url_part_list[2],
        "organization": url_part_list[3],
        "repository": url_part_list[4]
    }


def format_url(url):
    # Clean the protocol
    url_parts = get_url_parts(url)
    return "git@{domain}:{organization}/{repository}.git".format(**url_parts)


def clone_repos(repo_url_list):
    for url in repo_url_list:
        url = format_url(url)
        command = f"cd {URL_CLONE_PATH}; git clone {url} >/dev/null 2>&1"
        os.system(command)


def clean_repo_list_file():
    os.system(f": > {FILE_WITH_URLS}")


def open_repo_list_file():
    os.popen("open "+FILE_WITH_URLS).read


def open_cloned_path():
    os.system("open "+URL_CLONE_PATH)


if __name__ == "__main__":
    # Services
    service_prompt = ServicePrompt()

    service_prompt.welcome("Clone Repositories")
    open_repo_list_file()
    service_prompt.wait("Please fill the repository list file")
    repo_url_list = Utils.get_file_items(FILE_WITH_URLS)
    service_prompt.message(f"Found {len(repo_url_list)} repositoires in {FILE_WITH_URLS}")
    service_prompt.message("Process started")
    clone_repos(repo_url_list)
    clean_repo_list_file()
    service_prompt.message("Process finished")
    open_cloned_path()
