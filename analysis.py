import pandas as pd

def preprocess_price(price):
    # Remove non-numeric characters from the price string
    return float(price.replace('Rp', '').replace('.', ''))

def analyze_data(filename):
    # Read the data
    data = pd.read_excel(filename)

    # Preprocess 'Price' column
    data['Price'] = data['Price'].apply(preprocess_price)

    # Sort data by price and rating
    data_sorted_price = data.sort_values(by='Price')

    # Calculate summary statistics
    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    mean_rating = data['Rating'].mean()
    median_rating = data['Rating'].median()

    return data_sorted_price, mean_price, median_price, mean_rating, median_rating
