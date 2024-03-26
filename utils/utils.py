from datetime import datetime
import pandas as pd


class Utils:

    @classmethod
    def get_file_items(self, path):
        with open(path) as f:
            return f.readlines()

    @classmethod
    def write_file(self, path, body):
        with open(path, "w") as f:
            return f.write(body)

    @classmethod
    def get_timestamp(self):
        return datetime.utcnow().strftime("%d%b%y%H%M%S")

    @classmethod
    def get_time_standard(self):
        return datetime.utcnow().strftime("%d/%b/%Y %H:%M:%S")

    @classmethod
    def read_xlsx(self, path):
        df = pd.read_excel(path, sheet_name="components")
        return df.to_dict("records")

    @classmethod
    def write_xlsx(self, dic_list, path):
        with pd.ExcelWriter(path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df = pd.DataFrame.from_dict(dic_list)
            df.to_excel(writer, 'components', index=False)
