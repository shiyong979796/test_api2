from configparser import ConfigParser
import mypath


class HandleConfigParser:

    def __init__(self, file_path):
        self.conf_obj = ConfigParser()
        self.conf_obj.read(file_path, encoding='utf-8')

    def get_str(self, section, option):
        return self.conf_obj.get(section, option)

    def get_bool(self, section, option):
        return self.conf_obj.getboolean(section, option)

    def get_float(self, section, option):
        return self.conf_obj.getfloat(section, option)

    def get_int(self, section, option):
        return self.conf_obj.getint(section, option)


cf = HandleConfigParser(mypath.conf_file_dir)
base_url = cf.get_str('Url', 'PROD_URL')

if __name__ == '__main__':
    cf = HandleConfigParser(mypath.conf_file_dir)
    print(cf.get_str('Log', 'level'))
    print(base_url)