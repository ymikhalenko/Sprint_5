from locators import CreateLisitingPageLocators, MainPageLocators, ProfilePageLocators, RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import GET_WEB_ELEMENT_TIMEOUT, CITY


class TestCreateListingPage:
    def test_create_listing_regular_creation_creates_listing_in_profile(self, main_page_loged_in, fake_listing):
        main_page_loged_in.find_element(
            *MainPageLocators.add_listing_button).click()
        WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(CreateLisitingPageLocators.new_listing_title))
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.name_input).send_keys(fake_listing.get('name'))
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.description).send_keys(fake_listing.get('description'))
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.price).send_keys(fake_listing.get('price'))
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.category_drop_down).click()
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.category_book).click()
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.city_drop_down).click()
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.city_spb).click()
        main_page_loged_in.execute_script("arguments[0].click();", main_page_loged_in.find_element(
            *CreateLisitingPageLocators.condition_used))
        main_page_loged_in.find_element(
            *CreateLisitingPageLocators.create_listing_button).click()
        WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.search_filter))
        main_page_loged_in.find_element(
            *MainPageLocators.profile_photo).click()
        WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.my_profile_title))
        next_page_button = main_page_loged_in.find_element(
            *ProfilePageLocators.next_page_button)
        main_page_loged_in.execute_script(
            'arguments[0].scrollIntoView();',
            next_page_button
        )
        while next_page_button.get_attribute('disabled') is None:
            current_page = main_page_loged_in.find_element(
                *ProfilePageLocators.page_indicator).text
            next_page_button.click()
            WebDriverWait(main_page_loged_in, GET_WEB_ELEMENT_TIMEOUT).until(
                lambda driver: driver.find_element(
                    *ProfilePageLocators.page_indicator).text != current_page)
            next_page_button = main_page_loged_in.find_element(
                *ProfilePageLocators.next_page_button)
        last_listing_title = main_page_loged_in.find_element(
            *ProfilePageLocators.last_listing_title)
        last_listing_city = main_page_loged_in.find_element(
            *ProfilePageLocators.last_listing_city)
        last_listing_price = main_page_loged_in.find_element(
            *ProfilePageLocators.last_listing_price)
        assert last_listing_title.is_displayed() and last_listing_city.is_displayed(
        ) and last_listing_price.is_displayed() and last_listing_title.text == fake_listing.get('name') and last_listing_city.text == CITY and last_listing_price.text.replace(' ', '') == f"{fake_listing.get('price')}₽"
