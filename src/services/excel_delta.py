from tkinter.filedialog import askopenfilename
from utils import Utils
from tkinter import Tk
import pandas as pd
import os

REPORT_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/reports"


def menu_welcome():
    print("Welcome to the excel delta tool")


def get_report_path():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def get_file_name(file_path):
    return file_path.split("/")[-1]


def get_file_delta(file_path_a, file_path_b):
    dt_file_a = pd.read_excel(file_path_a)
    dt_file_b = pd.read_excel(file_path_b)
    file_name_a = get_file_name(file_path_a)
    file_name_b = get_file_name(file_path_b)

    print(
        f"Selected: \n* {get_file_name(file_path_a)} \n* {get_file_name(file_path_b)}\n\n")

    dt_delta = pd.merge(dt_file_a, dt_file_b, on="ID", how="right")

    filename = f"{REPORT_PATH}/delta_{file_name_a}_{file_name_b}_{Utils.get_timestamp()}.xlsx"
    dt_delta.to_excel(filename)

    print("report created successfully at "+filename+"\n\n")


if __name__ == "__main__":
    os.system("clear")
    file_path_a = get_report_path()
    file_path_b = get_report_path()
    get_file_delta(file_path_a, file_path_b)
