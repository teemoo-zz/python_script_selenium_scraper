# --1-- Imports and Setup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time
import glob

# --2-- Helper Function
def wait_and_print(message, seconds=3):
    print(message)
    time.sleep(seconds)

# --3-- Chrome Options Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# --4-- Download Directory Setup
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": desktop_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# --5-- WebDriver Initialization
try:
    wait_and_print("Initializing Chrome driver...")
    service = Service(ChromeDriverManager(version="latest").install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    print(f"Error initializing Chrome driver: {e}")
    print("Attempting to use default ChromeDriver path...")
    driver = webdriver.Chrome(options=chrome_options)

# --6-- Main Script Execution
try:
    # Step 1: Open Google Chrome Browser
    wait_and_print("Step 1: Opening Google Chrome Browser...")

    # Step 2: Go to the first URL
    wait_and_print("Step 2: Navigating to the first URL...")
    driver.get("https://opendata.hira.or.kr/home.do")
    wait_and_print("Arrived at the first URL.")

    # Step 3: Go to the second URL
    wait_and_print("Step 3: Navigating to the second URL...")
    driver.get("https://opendata.hira.or.kr/op/opc/olapMaterialTab3.do")
    wait_and_print("Arrived at the second URL.")

    # Step 4: Search for the element and click it
    wait_and_print("Step 4: Searching for the Excel button...")
    wait = WebDriverWait(driver, 10)
    excel_button = wait.until(EC.element_to_be_clickable((By.ID, "exlBtn")))
    wait_and_print("Excel button found. Clicking the button...")
    excel_button.click()

    # Step 5: Wait for the download to complete
    wait_and_print("Step 5: Waiting for the download to complete...", 30)

    # Step 6: Find the most recently downloaded file
    wait_and_print("Step 6: Searching for the downloaded file...")
    list_of_files = glob.glob(os.path.join(desktop_path, '*.xlsx'))  # Assuming it's an Excel file
    if not list_of_files:
        raise Exception("No Excel file was downloaded")
    
    latest_file = max(list_of_files, key=os.path.getctime)
    wait_and_print(f"Found the downloaded file: {latest_file}")

    # Step 7: Rename the file
    wait_and_print("Step 7: Renaming the file...")
    new_file_name = os.path.join(desktop_path, "downloaded_file.xlsx")
    os.rename(latest_file, new_file_name)

    wait_and_print(f"File downloaded and renamed to 'downloaded_file.xlsx' on the desktop.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    wait_and_print("Closing the browser...")
    driver.quit()

print("Script execution completed.")
