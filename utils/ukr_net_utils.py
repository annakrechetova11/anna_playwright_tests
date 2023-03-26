import copy
from utils.locators import SendEmailLocators
from playwright.sync_api import expect


class UkrNetEmail(SendEmailLocators):
    def __init__(self, page):
        self.page = page
        self.ukr_net_url = "https://mail.ukr.net"
        super(UkrNetEmail, self).__init__(page=page)

    def fill_the_email_data(self, email, subject_text):
        self.write_the_letter.click()
        if not isinstance(email, list):
            email = list(email)
        for address in email:
            self.email.fill(address)
            self.page.keyboard.press(key='Enter')
            self.email.fill(address)
        self.text_subject.fill(subject_text)

    def copy_and_paste_body_text(self, body_text):
        copied_text = copy.copy(body_text)
        self.body_field.fill(value=copied_text)

    def send_email(self):
        self.send_email_button.click()
        expect(self.letter_was_sent).to_be_visible()

