from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.tokopedia.com/find/laptop-gaming")

try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "css-ovjotx"))
    )

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write the headers to the worksheet
    worksheet.append(["Product Name", "Price", "Rating"])

    # Get current window height
    window_height = driver.execute_script("return window.innerHeight;")
    
    # Scroll down half the height of the window, 10 times
    for _ in range(10):
        driver.execute_script(f"window.scrollBy(0, {window_height/2});")
        time.sleep(5)  # Add a small pause between scrolls

    products = driver.find_elements(By.CLASS_NAME, "css-ovjotx")

    for product in products:
        try:
            nama = product.find_element(By.CSS_SELECTOR, ".prd_link-product-name.css-3um8ox").text
            harga = product.find_element(By.CSS_SELECTOR, ".prd_link-product-price.css-h66vau").text
            rating = product.find_element(By.CSS_SELECTOR, ".prd_rating-average-text.css-y301c6").text

            # Write the data to the worksheet
            worksheet.append([nama, harga, rating])

        except Exception as e:
            print(f"Error scraping product {product}: {e}")

except Exception as e:
    print(f"Error waiting for elements: {e}")

finally:
    driver.quit()

# Save the workbook to an Excel file
workbook.save("output.xlsx")
