from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

def get_timestamps(link):
    # Path to Edge WebDriver
    edge_driver_path = r"C:\Users\Parker\Downloads\edgedriver_win64 (1)\msedgedriver.exe"

    # Initialize Edge WebDriver using Service
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service)

    # Open the target website
    driver.get(link)

    # Wait for elements to load (adjust the locator as needed)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".style-scope.ytd-macro-markers-list-item-renderer"))
        )
        # Extract page source after elements are loaded
        html_source = driver.page_source
    finally:
        # Close the browser
        driver.quit()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_source, "html.parser")

    # Regex to match time values
    time_pattern = re.compile(r"^(?:\d+:)?\d{1,2}:\d{2}$") # Captures the time pattern of HH:MM:SS


    # Initialize the result list
    result = []

    # Locate all elements with the desired class
    elements = soup.find_all("div", class_="style-scope ytd-macro-markers-list-item-renderer")

    # Extract all time values and their associated titles
    for element in elements:
        if element.text and time_pattern.match(element.text.strip()):
            time_value = element.text.strip()
            
            # Find parent or sibling with a title attribute (adjust if necessary)
            parent_or_sibling = element.find_parent("h4") or element.find_previous_sibling("h4")
            title = parent_or_sibling["title"] if parent_or_sibling and parent_or_sibling.has_attr("title") else None
            
            # Append the result to the list
            result.append({"time": time_value, "title": title})

    return result

def processed_timestamps(link):
    timestamp_data = get_timestamps(link)
    processed_result = {}

    for i, item in enumerate(timestamp_data):
        if item['title'] != None:
            data = {item['title'] : item['time']}
            processed_result.update(data)
        else:
            pass

    return processed_result