import mypath
import os

from common.handle_excel import HandleExcel

# 获取register测试用例
register_case_dir = os.path.join(mypath.case_data_dir, 'register.xlsx')
register_case_data = HandleExcel(register_case_dir, 'sheet1').get_all_data()


if __name__ == '__main__':
    print(register_case_data)