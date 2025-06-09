
import os
# DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_DIR = DIR
CASE_DIR = os.path.join(DIR, 'testcase')
DATA_DIR = os.path.join(DIR, 'testdata')
LOG_DIR = os.path.join(DIR, 'testlog')
REPORT_DIR = os.path.join(DIR, 'testreport')


print(DIR)
print(os.path.join(DIR, 'config.ini'))