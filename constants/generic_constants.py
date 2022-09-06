"""
This page consists of Generic and Login page xpaths and constants
"""
from os.path import join, dirname

# locators #

ORIGIN = "//input[@id='txtOrigin']"



TEXT_PLACEHOLDER = "//input[@type='text']"
TEXT = "BUG_WARS"
BUTTON = "(//button[@type='button'])[2]"
VALID_LOGIN_URL = "http://uitestingplayground.com/sampleapp"
USER_NAME = "//input[@name='UserName']"
PASSWORD1 = "//input[@name='Password']"
LOGIN = "//button[@id='login']"

# Constants #
WAIT_TIME = 100


# Path #
DATA_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\test\\Data\\{}')
DOWNLOAD_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation/downloads/{}')
REPORT_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\report')




