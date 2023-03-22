from openpyxl import load_workbook
import mypath
import os


class HandleExcel:
    def __init__(self, file_path, sheet_name):
        sheet_list = load_workbook(os.path.join(file_path))
        self.sheet_data = sheet_list[sheet_name]

    def get_title(self):
        list_title = []
        for cell in list(self.sheet_data.rows)[0]:
            list_title.append(cell.value)
        return list_title

    def get_all_data(self):
        list_all_data = []
        for row in list(self.sheet_data.rows)[1:]:
            item = []
            for cell in row:
                item.append(cell.value)
            list_all_data.append(dict(zip(self.get_title(), item)))
        return list_all_data




if __name__ == '__main__':
    print(mypath.case_data_dir + 'register.xlsx')
    xl = HandleExcel(mypath.case_data_dir + '\\register.xlsx', 'Sheet1')
    title = xl.get_title()
    print(title)
    print(xl.get_all_data())
