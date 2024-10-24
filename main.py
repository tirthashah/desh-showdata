import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Create the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def login():
    try:
        driver.get("https://bitnbinary.bnbrun.com/dashboard")
        time.sleep(4)

        email_input = driver.find_element(By.XPATH, './/input[@name="email"]')
        email_input.send_keys("tirtha.shah@bitnbinary.com")

        password_input = driver.find_element(By.XPATH, './/input[@name="password"]')
        password_input.send_keys("Tirtha@12")

        sign_in = driver.find_element(By.XPATH, './/button[@id="kt_sign_in_submit"]')
        sign_in.click()
        logging.info("Logged in successfully.")
    except Exception as e:
        logging.error(f"Login failed: {e}")

def navigate_to_attendance():
    try:
        attendance_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Attendance"]'))
        )
        attendance_link.click()
        time.sleep(5)
        logging.info("Navigated to Attendance.")
    except Exception as e:
        logging.error(f"Failed to navigate to Attendance: {e}")

def navigate_to_projects_management():
    try:
        projects_management_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Projects Management"]'))
        )
        projects_management_menu.click()

        projects_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/a[@class="menu-link without-sub" and .//span[@class="menu-title" and normalize-space(text())="Projects"]]'))
        )
        projects_menu.click()

        view_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="badge badge-light-primary fw-bold me-auto px-4 py-3" and normalize-space(text())="View"]'))
        )
        view_button.click()
        logging.info("Navigated to Projects Management.")
    except Exception as e:
        logging.error(f"Failed to navigate to Projects Management: {e}")

def click_filter_select():
    try:
        filter_select_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/a[contains(text(),"Bit & Binary")]'))
        )
        filter_select_button.click()
        time.sleep(5)
        logging.info("Clicked on filter select.")
    except Exception as e:
        logging.error(f"Failed to click filter select: {e}")

def navigate_to_public_data():
    try:
        public_data_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="publicdata"]'))
        )
        public_data_link.click()
        time.sleep(5)
        logging.info("Navigated to Public Data.")
    except Exception as e:
        logging.error(f"Failed to navigate to Public Data: {e}")

def navigate_to_overview():
    try:
        organization_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Organization"]'))
        )
        organization_menu.click()

        overview = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Overview"]'))
        )
        overview.click()

        edit_profile = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_profile_details_view"]/div[1]/a
