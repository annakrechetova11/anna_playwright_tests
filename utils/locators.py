class LoginLocators(object):
    def __init__(self, page):
        self.login_field = page.get_by_label("Ім'я скриньки")
        self.password_field = page.get_by_label("Пароль")
        self.continue_button = page.get_by_role("button", name="Продовжити")
        self.iframe_checkbox_captcha = page.frame_locator("iframe[title=\"reCAPTCHA\"]").get_by_role("checkbox",
                                                                                        name="Я не робот")


class SendEmailLocators(object):
    def __init__(self, page):
        self.write_the_letter = page.get_by_role("button", name="Написати листа")
        self.email = page.locator("input[name=\"toFieldInput\"]")
        self.field_subject = page.locator("input[name=\"subject\"]")
        self.text_subject = page.locator("input[name=\"subject\"]")
        self.body_field = page.frame_locator("#mce_0_ifr").locator("#tinymce")
        self.send_email_button = page.locator("xpath=//div[@class='screen__content']//button[text()='Надіслати']")
        self.letter_was_sent = page.get_by_text(" надіслано")


