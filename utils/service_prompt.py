import os


class ServicePrompt:

    def welcome(self, script_name):
        os.system("clear")
        print("Welcome to Report Toolkit: "+script_name)
        print("=============================================\n\n")

    def message(self, message):
        print(message+"\n\n")

    def question(self, message):
        print("\n")
        return input(message+"\n")

    def clear(self):
        os.system("clear")

    def wait(self, message):
        print(""+message+"\n\n")
        input("Please press any key to continue ...")
        os.system("clear")
