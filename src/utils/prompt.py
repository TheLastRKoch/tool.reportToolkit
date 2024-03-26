from plyer import notification
from os import environ as env
import os


class UtilPrompt:
    def welcome(self, service_name):
        os.system("clear")
        print(f"Welcome to the service {service_name}")
        print("================================================\n\n")

    def press_key_continue(self):
        print("")
        print("================================================")
        print("          press any key to continue")
        input("================================================\n")
        os.system("clear")

    def clear(self):
        os.system("clear")

    def wait(self, body):
        os.system("clear")
        print(body)
        self.press_key_continue()

    def message(self, text):
        os.system("clear")
        print(text)

    def notification_info(self, message):
        notification.notify(
            title=env["APLICATION_NAME"],
            message=message,
            app_icon=None,
            timeout=10,
        )

    def notification_error(self, title, message):
        notification.notify(
            title=env["APLICATION_NAME"],
            message=message,
            app_icon=None,
            timeout=10,
        )
