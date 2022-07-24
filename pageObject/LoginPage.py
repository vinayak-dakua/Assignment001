from selenium.webdriver.common.by import By


class LoginPage:
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//button[@class='button-1 login-button']")
    # logout_button = (By.XPATH, "//a[contains(text(),'Logout')]" )
    logout_button = (By.XPATH,  "//*[@id='navbarText']/ul/li[3]/a")

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,UserId):
        self.driver.find_element(*LoginPage.email).clear()
        return self.driver.find_element(*LoginPage.email).send_keys(UserId)

    def setPassword(self,Password):
        self.driver.find_element(*LoginPage.password).clear()
        return self.driver.find_element(*LoginPage.password).send_keys(Password)

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.login_button).click()

    def clickLogout(self):
        return self.driver.find_element(*LoginPage.logout_button).click()









