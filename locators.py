from selenium.webdriver.common.by import By


class MainPageLocators:
    logo = (
        By.XPATH, "//*[local-name()='svg' and starts-with(@class, 'header_logo')]")
    login_and_registration_button = (
        By.XPATH, "//button[text()='Вход и регистрация']")
    add_adv_button = (
        By.XPATH, "//button[text()='Разместить объявление']")
    username_and_profile_photo_row = "//div[contains(@class, 'flexRow')]"
    username = (
        By.XPATH, f"{username_and_profile_photo_row}//h3[starts-with(@class, 'profileText name')]")
    profile_photo = (
        By.XPATH, f"{username_and_profile_photo_row}//*[local-name()='svg' and contains(@class, 'svgSmall')]")
    logout_button = (
        By.XPATH, f"{username_and_profile_photo_row}//button[text()='Выйти']")


class LoginPageLocators:
    login_form = "//form[starts-with(@class,'popUp_shell')]"
    login_title = (
        By.XPATH, f"{login_form}//h1[text()='Войти']")
    email_input = (
        By.XPATH, f"{login_form}//input[@name='email']")
    password_input = (
        By.XPATH, f"{login_form}//input[@name='password']")
    login_button = (
        By.XPATH, f"{login_form}//button[text()='Войти']")
    no_account_button = (
        By.XPATH, f"{login_form}//button[text()='Нет аккаунта']")


class RegistrationPageLocators:
    registration_form = "//form[starts-with(@class,'popUp_shell')]"
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


class CreateLisitingPageLocators:
    pass
