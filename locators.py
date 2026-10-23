from selenium.webdriver.common.by import By
from constants import CITY


class MainPageLocators:
    logo = (
        By.XPATH, "//*[local-name()='svg' and contains(@class, 'header_logo')]")
    login_and_registration_button = (
        By.XPATH, "//button[text()='Вход и регистрация']")
    add_listing_button = (
        By.XPATH, "//button[text()='Разместить объявление']")
    username_and_profile_photo_row = "//div[contains(@class, 'flexRow')]"
    username = (
        By.XPATH, f"{username_and_profile_photo_row}//h3[contains(@class, 'profileText name')]")
    profile_photo = (
        By.XPATH, f"{username_and_profile_photo_row}//button[contains(@class, 'circleSmall')]")
    logout_button = (
        By.XPATH, f"{username_and_profile_photo_row}//button[text()='Выйти']")
    search_filter = (
        By.XPATH, "//form[contains(@class, 'filter_shell')]")


class LoginPageLocators:
    login_form = "//form[contains(@class,'popUp_shell')]"
    login_title = (
        By.XPATH, f"{login_form}//h1[text()='Войти']")
    login_to_add_listing_title = (
        By.XPATH, f"{login_form}//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    email_input = (
        By.XPATH, f"{login_form}//input[@name='email']")
    password_input = (
        By.XPATH, f"{login_form}//input[@name='password']")
    login_button = (
        By.XPATH, f"{login_form}//button[text()='Войти']")
    no_account_button = (
        By.XPATH, f"{login_form}//button[text()='Нет аккаунта']")


class RegistrationPageLocators:
    registration_form = "//form[contains(@class,'popUp_shell')]"
    registration_title = (
        By.XPATH, f"{registration_form}//h1[text()='Зарегистрироваться']")
    email_input = (
        By.XPATH, f"{registration_form}//input[@name='email']")
    password_input = (
        By.XPATH, f"{registration_form}//input[@name='password']")
    submit_password_input = (
        By.XPATH, f"{registration_form}//input[@name='submitPassword']")
    create_account_button = (
        By.XPATH, f"{registration_form}//button[text()='Создать аккаунт']")
    input_error_frame = (
        By.XPATH, f"{registration_form}//div[contains(@class,'input_inputError')]")
    error_text = (
        By.XPATH, f"{registration_form}//span[text()='Ошибка']")


class CreateLisitingPageLocators:
    new_listing_title = (
        By.XPATH, "//h1[text()='Новое объявление']")
    name_input = (
        By.XPATH, "//input[@name='name']")
    create_listing_line = "div[contains(@class, 'createListing_inputRow')]"
    category_drop_down = (
        By.XPATH, f"//{create_listing_line}//div[contains(@class, 'dropDownMenu_dropMenu')]//button[contains(@class,'dropDownMenu_arrowDown')]")
    category_book = (
        By.XPATH, f"//{create_listing_line}//div[contains(@class, 'dropDownMenu_options')]//button[span[text() = 'Книги']]")
    condition_used = (
        By.XPATH, "//input[@name='condition' and @value='Б/У']")
    city_drop_down = (
        By.XPATH, f"//div[contains(@class, 'dropDownMenu_dropMenu') and not(ancestor::{create_listing_line})]//button[contains(@class,'dropDownMenu_arrowDown')]")
    city_spb = (
        By.XPATH, f"//div[contains(@class, 'dropDownMenu_dropMenu') and not(ancestor::{create_listing_line})]//button[span[text() = '{CITY}']]")
    description = (
        By.XPATH, "//textarea[@name='description']")
    price = (
        By.XPATH, "//input[@name='price']")
    create_listing_button = (
        By.XPATH, "//button[text()='Опубликовать']")


class ProfilePageLocators:
    my_profile_title = (
        By.XPATH, "//h1[text()='Мой профиль']")
    my_listings_block = "//div[contains(@class, 'profilePage_listningBlock') and .//h1[text()='Мои объявления']]"
    last_card = f"({my_listings_block}//div[@class='card'])[last()]"
    last_listing_title = (
        By.XPATH, f"{last_card}//div[@class='about']//h2")
    last_listing_city = (
        By.XPATH, f"{last_card}//div[@class='about']//h3")
    last_listing_price = (
        By.XPATH, f"{last_card}//div[@class='price']//h2")
    page_indicator = (
        By.XPATH, f"{my_listings_block}//p[contains(@class, 'spanGlobal')]")
    next_page_button = (
        By.XPATH, f"{my_listings_block}//button[contains(@class, 'arrowButton--right')]")
