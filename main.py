import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def login():
    driver.get("https://bitnbinary.bnbrun.com/dashboard")
    time.sleep(4)

    email_input = driver.find_element(By.XPATH, './/input[@name="email"]')
    email_input.send_keys("tirtha.shah@bitnbinary.com")

    password_input = driver.find_element(By.XPATH, './/input[@name="password"]')
    password_input.send_keys("Tirtha@12")

    sign_in = driver.find_element(By.XPATH, './/button[@id="kt_sign_in_submit"]')
    sign_in.click()

def navigate_to_attendance():
    attendance_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Attendance"]'))
    )
    attendance_link.click()

    time.sleep(5)

def navigate_to_projects_management():
    projects_management_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Projects Management"]')) )
    projects_management_menu.click()

    projects_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[@class="menu-link without-sub" and .//span[@class="menu-title" and normalize-space(text())="Projects"]]')) )
    projects_menu.click()

    view_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'.//span[@class="badge badge-light-primary fw-bold me-auto px-4 py-3" and normalize-space(text())="View"]')))
    view_button.click()

def click_filter_select():
    filter_select_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[contains(text(),"Bit & Binary")]'))
    )
    filter_select_button.click()
    time.sleep(5)

def navigate_to_public_data():

    public_data_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="publicdata"]')) )

    public_data_link.click()

    time.sleep(5)

def navigate_to_overview():
    organization_menu = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Organization"]')) )
    organization_menu.click()

    overview =WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Overview"]')) )
    overview.click()

    edit_profile =WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_profile_details_view"]/div[1]/a')) )
    edit_profile.click()

    description =WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,'.// textarea[@formcontrolname = "description"]')) )
    description.send_keys("about work")

    checkboxes = [
        ('.//input[@type="checkbox" and @formcontrolname="show_products_in_bnbmart"]'),
        ('.//input[@type="checkbox" and @formcontrolname="show_price_in_bnbmart"]'),
        ('.//input[@type="checkbox" and @formcontrolname="show_jobs_in_bnbhiring"]')
    ]

    for checkbox_xpath in checkboxes:
        checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkbox_xpath))
        )
        # Scroll to the checkbox to ensure it’s in view
        ActionChains(driver).move_to_element(checkbox).perform()

        # Check if the checkbox is already selected, if not, click it
        if not checkbox.is_selected():
            checkbox.click()


    save_changes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_account_profile_details"]/form/div/div[15]/div[2]/button'))
    )
    ActionChains(driver).move_to_element(save_changes).perform()
    time.sleep(2)
    save_changes.click()


def go_to_documents():
        # Wait for the 'Documents' link to be clickable
        documents_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="#kt_app_sidebar_menu"]/div[3]/div[1]/div/div/div[2]/a/span[2]')) )
        documents_link.click()

        file_upload_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"File Upload")]')))
        file_upload_link.click()

        time.sleep(10)
        identy_name= WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'.//input[@formcontrolname="identification_name"]')) )
        identy_name.send_keys("documents")

        expiry_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/input[@formcontrolname="identification_expiry"]')))
        expiry_date.send_keys("5/12/2024")

        upload_header = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//h4[contains(text(),"Click here to upload")]')))
        upload_header.click()

def upload_file(file_path):
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file" and @name="resume"]'))  # Adjust if necessary
    )


    file_input.send_keys(file_path)
    print(f"File uploaded: {file_path}")

    time.sleep(10)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Submit")]'))
    )
    submit_button.click()

    time.sleep(2)



def main():
    login()
    navigate_to_attendance()
    navigate_to_projects_management()
    click_filter_select()
    navigate_to_public_data()
    navigate_to_overview()
    go_to_documents()

    file_path = os.path.abspath("/home/user/abc.txt")
    upload_file(file_path)

    time.sleep(100)
    driver.quit()


# Call the main function to execute the script
if __name__ == "__main__":
    main()
