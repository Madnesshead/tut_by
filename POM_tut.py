from web_elements import (
    InputField,
    SwitchButton,
    DropDownMenu,
    Link,
    ToggleButton,
    ImageLink,
    SharedToggleButton,
    MenuLink,
)


class MailLoginTutPage:
    _URL = 'https://mail.tut.by'

    faq_size = Link('a:contains("Ящик неограниченного размера")')
    faq_name = Link('a:contains("имяпользователя@tut.by")')
    faq_protocols = Link('a:contains("Поддержка протоколов POP3, IMAP4, SMTP, WAP, Web")')
    faq_safety = Link('a:contains("АнтиВирус, АнтиСпам, фильтры")')
    faq_resources = Link('a:contains("Единые имя и пароль для ресурсов портала TUT.BY")')

    email_register = ToggleButton('a > span[class="button linkRegButton gradientforbutton"]')
    email_login = InputField('#Username')
    email_password = InputField('#Password')
    email_recover_password = Link('div[class="forgot"] > a:contains("Восстановить забытый пароль »")')
    email_remember_checkbox = InputField('#memory')
    email_submit = ToggleButton('div > input[class="button loginButton gradientforbutton"]')

    auto = ImageLink('img.rSprite.res1752')
    shop = ImageLink('img[alt="Магазины"]')
    building = ImageLink('img[alt="Строительство"]')
    aviatickets = ImageLink('img.rSprite res1582')
    realty = ImageLink('img[alt="Недвижимость"]')
    tv_programmes = ImageLink('img[alt="ТВ-программа"]')
    auction = ImageLink('img[alt="Аукционы"]')
    news = ImageLink('img[alt="Новости"]')
    tourism = ImageLink('img[alt="Туризм"]')
    playbill = ImageLink('img[alt="Афиша"]')
    forty_two = ImageLink('img[alt="42"]')
    finance = ImageLink('img[alt="Финансы"]')
    maps = ImageLink('img[alt="Карты"]')
    weather = ImageLink('img[alt="Погода"]')
    tam = ImageLink('img[alt="TAM.BY"]')
    job = ImageLink('img[alt="Работа"]')
    lady = ImageLink('img[alt="Леди"]')
    sport = ImageLink('img[alt="Спорт"]')
    all_resources = ToggleButton('a[class="smallButton"] > span:contains("Все ресурсы")')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self._URL)
