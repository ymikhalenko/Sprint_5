from locators import MainPageLocators, RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import GET_WEB_ELEMENT_TIMEOUT, REGISTRATION_ERROR_FRAMES_COUNT


class TestRegistrationPage:
    def test_registration_regular_registration_username_appears(self, registration_page, fake_creds):
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

    def test_registration_nonformat_email_registration_shows_error(self, registration_page, fake_string, fake_creds):
        registration_page.find_element(
            *RegistrationPageLocators.email_input).send_keys(fake_string)
        registration_page.find_element(
            *RegistrationPageLocators.password_input).send_keys(fake_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.submit_password_input).send_keys(fake_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.create_account_button).click()
        error_text = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.error_text))
        error_frames = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_all_elements_located(RegistrationPageLocators.input_error_frame))
        assert error_text.is_displayed() and all(error_frame.is_displayed()
                                                 for error_frame in error_frames) and len(error_frames) == REGISTRATION_ERROR_FRAMES_COUNT

    def test_registration_registered_email_registration_shows_error(self, registration_page, existing_creds):
        registration_page.find_element(
            *RegistrationPageLocators.email_input).send_keys(existing_creds.get('email'))
        registration_page.find_element(
            *RegistrationPageLocators.password_input).send_keys(existing_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.submit_password_input).send_keys(existing_creds.get('password'))
        registration_page.find_element(
            *RegistrationPageLocators.create_account_button).click()
        error_text = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.error_text))
        error_frames = WebDriverWait(registration_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_all_elements_located(RegistrationPageLocators.input_error_frame))
        assert error_text.is_displayed() and all(error_frame.is_displayed()
                                                 for error_frame in error_frames) and len(error_frames) == REGISTRATION_ERROR_FRAMES_COUNT
