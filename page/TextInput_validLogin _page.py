import time
from datetime import timedelta, date

import allure

from base.basePage import BasePage
from constants import generic_constants as GC
from page.genericFunctions import GenericFunctions


class DocumentPage(BasePage):
    """
    This class of consists of reusable functions which can be used in Document creation and submission flow
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)

    @allure.step("UITAP")
    def UI_TAP(self):
        self.click_and_type(GC.TEXT_PLACEHOLDER, GC.TEXT)
        self.click(GC.BUTTON)


    def assert_text(self):
        button_text = self.get_text(GC.BUTTON)
        assert GC.TEXT == button_text



    def valid_login(self):
        self.launch_url(GC.VALID_LOGIN_URL)
        self.click_and_type(GC.USER_NAME, "test")
        self.click_and_type(GC.PASSWORD1, "password")
        self.click(GC.LOGIN)


