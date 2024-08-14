# Web Scraping Automation Script

This Python script automates the process of downloading an Excel file from a specific website using Selenium WebDriver and BeautifulSoup. The script performs the following steps:

1. Initializes a Chrome browser.
2. Navigates to two specified URLs.
3. Clicks on an Excel download button.
4. Waits for the file to download.
5. Renames the downloaded file to `downloaded_file.xlsx` and saves it to the desktop.

## Requirements

Before running the script, ensure that you have the following installed:

- Python 3.x
- Google Chrome browser

### Python Packages

You can install the required Python packages using pip:

```bash
pip install selenium webdriver_manager beautifulsoup4
