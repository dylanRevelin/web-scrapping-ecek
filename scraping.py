from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

def scrape_products(product_name, pages=1):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write the headers to the worksheet
    worksheet.append(["Product Name", "Price", "Rating"])

    try:
        for i in range(pages):
            try:
                driver.get(f"https://www.tokopedia.com/find/{product_name}?page={i+1}")
                WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-ovjotx"))
                )

                # Get current window height
                window_height = driver.execute_script("return window.innerHeight;")
                
                # Scroll down half the height of the window, 10 times
                for _ in range(5):
                    driver.execute_script(f"window.scrollBy(0, {window_height/0.5});")
                    time.sleep(2)  # Add a small pause between scrolls

                products = driver.find_elements(By.CSS_SELECTOR, ".css-ovjotx")

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
        # Save the workbook to an Excel file
        filename = f"{product_name}_output.xlsx"
        workbook.save(filename)

        # Close the webdriver
        driver.quit()
        
        return filename
