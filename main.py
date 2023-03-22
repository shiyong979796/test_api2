import pytest
import mypath
import pytest_html

# pytest.main(['-s', '-v', '--reruns', "2", '--reruns-delay', '5', r'--alluredir=output\allure_dir'])
# pytest.main(['-s', '-v', r'--alluredir=.output\allure_dir'])
pytest.main(['-s', '-v', '--reruns', "2", '--reruns-delay', '5', r'--alluredir=out_put\allure_dir'])