
import os
# DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_DIR = DIR
CASE_DIR = os.path.join(DIR, 'testCase')
DATA_DIR = os.path.join(DIR, 'testData')
LOG_DIR = os.path.join(DIR, 'testLog')
REPORT_DIR = os.path.join(DIR, 'testReport')


print(DIR)
print(os.path.join(DIR, 'config.ini'))