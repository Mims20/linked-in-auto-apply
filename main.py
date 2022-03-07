import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver_path = "C:\chromedriver_win32\chromedriver.exe"  # chrome driver location
driver = webdriver.Chrome(executable_path=driver_path)

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&keywords=python%20developer&location=Worldwide"
driver.get(URL)

EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
time.sleep(2)
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL, Keys.TAB, PASSWORD, Keys.ENTER)

time.sleep(3)

# all_jobs = driver.find_elements(By.CSS_SELECTOR, ".base-card__full-link")
# for job in all_jobs:

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

for listing in all_listings:
    print("called")
    print(listing.text)
    listing.click()
    time.sleep(3)

    try:
        apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button span')
        apply.click()

        phone = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text div input ")
        # fill phone number form if empty
        if phone.text == "":
            phone.send_keys("0202268754")

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # if submit button is next button, then skip
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__icon")
            close_button.click()
            try:
                discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
            except IndexError:
                discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                discard_button.click()
            print("Complex application, skipped")
            time.sleep(2)
            continue

        else:
            submit_button.click()

            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__icon")
            close_button.click()
            try:
                discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
            except IndexError:
                discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                discard_button.click()
            time.sleep(2)
    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped")
        time.sleep(2)

# driver.quit()
