import allure
from allure_commons.types import Severity
from qa_guru_python_13.model.pages.registration_pages import RegistrationPage
from qa_guru_python_13.data import users


@allure.tag('DemoQa')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('User registration')
@allure.story('Register new user')
@allure.link('https://demoqa.com', name='Testing')
def test_user_registration_form():
    client = users.user
    registration_pages = RegistrationPage()

    with allure.step('Открытие страницы регистрации'):
        registration_pages.open()

    with allure.step('Регистрация пользователя'):
        registration_pages.registration_form_page(client)

    with allure.step('Проверка регистрации пользователя'):
        registration_pages.should_registration_form(client)
