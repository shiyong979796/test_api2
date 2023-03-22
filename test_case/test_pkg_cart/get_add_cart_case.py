from common.handle_excel import HandleExcel
from mypath import case_data_dir
import os

cart_path = os.path.join(case_data_dir, 'cart.xlsx')
add_cart_case_data = HandleExcel(cart_path, 'add_goods_to_cart').get_all_data()

if __name__ == '__main__':

    print(type(add_cart_case_data[0]))
