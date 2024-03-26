from os import environ as env
from datetime import datetime
import pandas
import csv
import os


class UtilFile:
    def read_text_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def read_text_file_as_list(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().split("\n")

    def write_text_file(self, path, body):
        with open(path, "w") as f:
            f.write(body)

    def write_csv(self, path, data):
        if not os.path.exists(path):
            os.system(f"touch '{path}'")

        with open(path, "w", newline="") as f:
            f.write("sep=,\n")
            csv_writer = csv.writer(f)

            # Write separator
            header = data[0].keys()
            csv_writer.writerow(header)

            for item in data:
                csv_writer.writerow(item.values())

    def read_excel(self, path, sheet_name):
        return pandas.read_excel(path, sheet_name=sheet_name)

    def filter_by_column(self, excel_df: pandas.DataFrame, column_name, query):
        return excel_df[excel_df[column_name] == query]

    def get_one_column_excel(self, excel_df: pandas.DataFrame, column_name):
        return excel_df[column_name].to_list()

    def clear_file_content(self, path):
        os.system(f"echo > {path}")

    def timestamp_filename(self, filename):
        return env[filename].format(
            timestamp=datetime.utcnow().strftime("%d%b%y%H%M%S")
        )
