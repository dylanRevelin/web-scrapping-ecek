from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

def scrape_tokopedia(driver, product_name, pages, worksheet):
    for i in range(pages):
        try:
            driver.get(f"https://www.tokopedia.com/find/{product_name}?page={i+1}")
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-ovjotx"))
            )

            window_height = driver.execute_script("return window.innerHeight;")
            for _ in range(5):
                driver.execute_script(f"window.scrollBy(0, {window_height/0.5});")
                time.sleep(2)

            products = driver.find_elements(By.CSS_SELECTOR, ".css-ovjotx")

            for product in products:
                try:
                    nama = product.find_element(By.CSS_SELECTOR, ".prd_link-product-name.css-3um8ox").text
                    harga = product.find_element(By.CSS_SELECTOR, ".prd_link-product-price.css-h66vau").text
                    rating = product.find_element(By.CSS_SELECTOR, ".prd_rating-average-text.css-y301c6").text
                    worksheet.append(["Tokopedia", nama, harga, rating])
                except Exception as e:
                    print(f"Error scraping product {product}: {e}")
        except Exception as e:
            print(f"Error waiting for elements on Tokopedia: {e}")

def scrape_bukalapak(driver, product_name, pages, worksheet):
    for i in range(pages):
        try:
            driver.get(f"https://www.bukalapak.com/products?page={i+1}&search%5Bkeywords%5D={product_name}")
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "bl-flex-item"))
            )

            window_height = driver.execute_script("return window.innerHeight;")
            for _ in range(5):
                driver.execute_script(f"window.scrollBy(0, {window_height});")
                time.sleep(2)

            products = driver.find_elements(By.CLASS_NAME, "bl-flex-item")

            for product in products:
                try:
                    nama = product.find_element(By.CLASS_NAME, "bl-text").text
                    harga = product.find_element(By.CLASS_NAME, "bl-product-card-new__price").text
                    rating_text = product.find_element(By.CLASS_NAME, "bl-product-card-new__ratings").text
                    rating = rating_text[0] if rating_text[0] != "T" else "0"
                    worksheet.append(["Bukalapak", nama, harga, rating])
                except Exception as e:
                    print(f"Error scraping product {product}: {e}")
        except Exception as e:
            print(f"Error waiting for elements on Bukalapak: {e}")

def scrape_products(product_name, pages=1):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    worksheet.append(["Website", "Product Name", "Price", "Rating"])

    try:
        scrape_tokopedia(driver, product_name, pages, worksheet)
        scrape_bukalapak(driver, product_name, pages, worksheet)
    finally:
        filename = f"{product_name}_output.xlsx"
        workbook.save(filename)
        driver.quit()
        
        return filename
