import pandas as pd

def analyze_data(filename):
    # Read the data
    data = pd.read_excel(filename)

    # 1. Exploratory Data Analysis (EDA)
    data_info = data.info()
    data_desc = data.describe()

    # 2. Clean 'Price' column
    data['Price'] = data['Price'].str.replace('Rp', '').str.replace('.', '').astype(float)

    # 3. Summary Statistics
    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    mean_rating = data['Rating'].mean()
    median_rating = data['Rating'].median()

    # 4. Data Visualization
    # Add your data visualization code here if needed

    return data_info, data_desc, mean_price, median_price, mean_rating, median_rating
