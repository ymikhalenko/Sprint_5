from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import GET_WEB_ELEMENT_TIMEOUT, REGISTRATION_ERROR_FRAMES_COUNT


class TestLoginPage:
    def test_login_existing_creds_username_appears(self, login_page, existing_creds):
        login_page.find_element(
            *LoginPageLocators.email_input).send_keys(existing_creds.get('email'))
        login_page.find_element(
            *LoginPageLocators.password_input).send_keys(existing_creds.get('password'))
        login_page.find_element(
            *LoginPageLocators.login_button).click()
        username = WebDriverWait(login_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.username))
        profile_photo = WebDriverWait(login_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.profile_photo))
        login_popup_is_invisible = WebDriverWait(login_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(
                LoginPageLocators.login_title))
        assert username.is_displayed() and profile_photo.is_displayed(
        ) and login_popup_is_invisible
