from utils.locators import LoginLocators
from time import sleep, time


class Login(LoginLocators):
    def __init__(self, page):
        self.page = page
        super(Login, self).__init__(page=page)

    def login(self, password, login):
        self.login_field.fill(login)
        self.password_field.fill(password)
        self.continue_button.click()
        self.iframe_checkbox_captcha.click()

    @staticmethod
    def login_check(context, timeout=120):
        found = False
        current_time = time()
        while current_time + timeout > time():
            cookies = context.cookies()
            if [cookie for cookie in cookies if cookie["domain"].startswith(".accounts.ukr.net")]:
                found = True
                break
            else:
                sleep(0.5)
        if not found:
            raise Exception("User is not logged in after {}".format(timeout))


