import unittest
from selenium import webdriver
from pages import LoginPage
import time
import smtplib

# Please, fill in sender, receiver emails and sender password
sender_email = ""
sender_password = ""
receiver_email = ""


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_tut_login_success(self):
        login_page = LoginPage(self.browser)
        login_page_contents = login_page.login("python.rulezz@tut.by", "Auto12345678")
        time.sleep(5)
        self.assertIn("Входящие", login_page_contents)

    def test_tut_login_not_success(self):
        login_page = LoginPage(self.browser)
        login_page_contents = login_page.login("python.rulezz@tut.by", "Auto")
        self.assertIn("Неверное имя пользователя или пароль", login_page_contents)

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    with open('report.txt', 'w') as outfile:
        unittest.TextTestRunner(stream=outfile, verbosity=2).run(suite)

    # Send report
    with open('report.txt', 'r') as infile:
        server = smtplib.SMTP('smtp.yandex.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        subject = 'Test report'
        email_text = infile.read()
        message = f"""From: {sender_email}\nTo: {receiver_email}\nSubject: {subject}\n\n{email_text}"""
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
