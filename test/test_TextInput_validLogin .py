import pytest

from page.genericFunctions import GenericFunctions
from page.genericFunctions import GenericFunctions


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestDocumentCreation:

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.dp = DocumentPage(self.driver)


    def test_ui_tap(self):
        self.dp.UI_TAP()
        self.dp.assert_text()


    def test_valid_login_url(self):
        """
        NEGATIVE SCENARIO
        :return:
        """
        self.dp.valid_login()





