import pandas as pd

def preprocess_price(price):
    return float(price.replace('Rp', '').replace('.', '').replace(',', '').strip())

def analyze_data(filename):
    # Read the data
    data = pd.read_excel(filename)

    # Preprocess 'Price' column
    data['Price'] = data['Price'].apply(preprocess_price)

    # Convert 'Rating' column to numeric if it isn't already
    data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

    # Sort data by price and rating
    data_sorted_price = data.sort_values(by='Price')

    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    mean_rating = data['Rating'].mean()
    median_rating = data['Rating'].median()
    highest_price = data['Price'].max()
    lowest_price = data['Price'].min()

    return data_sorted_price, mean_price, median_price, mean_rating, median_rating, highest_price, lowest_price