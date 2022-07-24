import time
import pytest

from TestData.LoginPageTestData import getTestData
from pageObject.LoginPage import LoginPage
from utility.BaseClass import BaseClass


class Test_Login(BaseClass):
    A_Condition = []
    @pytest.mark.parametrize("UserId, Password, E_Condition", getTestData())
    def test_login(self, setup, UserId, Password, E_Condition):
        A_Condition = ""
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.verifyThePage()
        log.info("We are in correct page")
        loginPage.setUserName(UserId)
        loginPage.setPassword(Password)
        loginPage.clickLogin()
        txt = self.driver.title
        if txt == "Dashboard / nopCommerce administration":
            loginPage.clickLogout()
            time.sleep(5)
            Status = A_Condition + "Pass"
        else:
            Status = A_Condition + "Fail"

        if Status == E_Condition:
            assert True

        else:
            assert False







