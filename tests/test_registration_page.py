from locators import MainPageLocators, RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import GET_WEB_ELEMENT_TIMEOUT


class TestRegistrationPage:
    def test_registration_regular_registration_logins(self, registration_page, fake_creds):
        registration_page.find_element(
            *RegistrationPageLocators.email_input).send_keys(fake_creds.get('email'))
        registration_page.find_element(
            *RegistrationPageLocators.password_input).send_keys(fake_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.submit_password_input).send_keys(fake_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.create_account_button).click()
        username = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.username))
        profile_photo = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.profile_photo))
        registration_popup_is_invisible = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(
                RegistrationPageLocators.registration_title))
        assert username.is_displayed() and profile_photo.is_displayed(
        ) and registration_popup_is_invisible
