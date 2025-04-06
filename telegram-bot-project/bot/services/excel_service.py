class ExcelService:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_excel_file(self):
        import pandas as pd
        df = pd.DataFrame(columns=["Date", "Hours Worked", "Description"])
        df.to_excel(self.file_path, index=False)

    def log_hours(self, date, hours_worked, description):
        import pandas as pd
        df = pd.read_excel(self.file_path)
        new_entry = {"Date": date, "Hours Worked": hours_worked, "Description": description}
        df = df.append(new_entry, ignore_index=True)
        df.to_excel(self.file_path, index=False)

    def get_hours_logged(self):
        import pandas as pd
        df = pd.read_excel(self.file_path)
        return df