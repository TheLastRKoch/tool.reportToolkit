from utils.command import UtilCommand
from utils.prompt import UtilPrompt
from utils.file import UtilFile

URL_LIST_PATH = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/URLs.txt"
NUM_OF_URL = 15


class OpenURLList:
    def remove_duplicates(self, url_list):
        return list(set(url_list))

    def open_urls(self, url_list):
        command = UtilCommand()

        count = 1
        formatterd_list = list(dict.fromkeys(url_list))
        for idx, url in enumerate(formatterd_list):
            if count == NUM_OF_URL:
                input(
                    f"{idx+1}/{len(formatterd_list)} URLs opened press any key to continue"
                )
                count = 0
            command.open(url)
            count = count + 1

    def run(self):
        # Service definition
        prompt = UtilPrompt()
        file = UtilFile()
        command = UtilCommand()

        prompt.welcome("Open URL list")
        command.open(URL_LIST_PATH)
        prompt.wait("Please fill the URL list file")
        url_list = self.remove_duplicates(file.read_text_file_as_list(URL_LIST_PATH))
        prompt.message(f"Found {len(url_list)} unique URLs\n")
        self.open_urls(url_list)
        file.clear_file_content(URL_LIST_PATH)
