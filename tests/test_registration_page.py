from pages.registration_page import RegistrationPage
from users import create_student
import allure

@allure.title("Successful registration_form")
def test_student_registration_form(browser_setup):
    registration_page = RegistrationPage()
    student = create_student()

    # WHEN
    with allure.step("open registration page"):
        registration_page.open()

    with allure.step("enter student name"):
        registration_page.register(student)

    with allure.step("click submit"):
        registration_page.submit()
    # THEN
    with allure.step("check results"):
        registration_page.should_have_registered(student)

