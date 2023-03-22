import os


# 项目基础路径
base_dir = os.path.dirname(os.path.abspath(__file__))

# case_data 路径
case_data_dir = os.path.join(base_dir, 'case_data')

# test_case 路径
test_case_dir = os.path.join(base_dir, 'test_case')

# log_filer路径
log_file_dir = os.path.join(base_dir, 'out_put', 'log_file')

# 配置文件路径
conf_file_dir = os.path.join(base_dir, 'conf_file', 'conf_file.ini')

# allure_dir 路径
allure_report_dir = os.path.join(base_dir,'out_put','allure_dir')

# csv 文件路径
prime_data_dir = os.path.join(base_dir, 'prime_data')


if __name__ == '__main__':
    print(case_data_dir)

    print(log_file_dir)

    print(allure_report_dir)