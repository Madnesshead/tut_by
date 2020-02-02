from POM_tut import MailLoginTutPage


class LoginPage:

    def __init__(self, browser):
        self.mail_page = MailLoginTutPage(browser)

    def set_email(self, email):
        self.mail_page.email_login.send_keys(email)

    def set_password(self, password):
        self.mail_page.email_password.send_keys(password)

    def click_submit(self):
        self.mail_page.email_submit.click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit()
        return self.mail_page.driver.page_source
