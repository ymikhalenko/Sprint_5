from locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import GET_WEB_ELEMENT_TIMEOUT


class TestMainPage:
    def test_main_page_logout_removes_username(self, main_page_loged_in):
        main_page_loged_in.find_element(
            *MainPageLocators.logout_button).click()
        username = WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(MainPageLocators.username))
        profile_photo = WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(MainPageLocators.profile_photo))
        login_button = WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.login_and_registration_button))
        assert username and profile_photo and login_button

    def test_add_adv_logged_out_user_login_form_appears(self, main_page):
        main_page.find_element(
            *MainPageLocators.add_listing_button).click()
        assert WebDriverWait(main_page, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.login_to_add_listing_title)).is_displayed()
