import pandas as pd

# Read the data
data = pd.read_excel('output.xlsx')

# 1. Exploratory Data Analysis (EDA)
print(data.info())
print(data.describe())

# 2. Clean 'Price' column
data['Price'] = data['Price'].str.replace('Rp', '').str.replace('.', '').astype(float)

# 3. Summary Statistics
print("Mean price:", data['Price'].mean())
print("Median price:", data['Price'].median())
print("Mean rating:", data['Rating'].mean())
print("Median rating:", data['Rating'].median())

# 4. Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Price'], bins=20, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price (Rp)')
plt.ylabel('Frequency')
plt.show()

# Rating Distribution
plt.figure(figsize=(6, 4))
sns.histplot(data['Rating'], bins=5, kde=True)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# 5. Top Products by Price and Rating
top_price = data.nlargest(5, 'Price')
top_rating = data.nlargest(5, 'Rating')

print("Top 5 products by price:")
print(top_price[['Product Name', 'Price']])
print("\nTop 5 products by rating:")
print(top_rating[['Product Name', 'Rating']])

# 6. Price Range Analysis
price_ranges = pd.cut(data['Price'], bins=[0, 5000000, 10000000, 15000000, 20000000, 25000000, float('inf')], 
                      labels=['<5M', '5M-10M', '10M-15M', '15M-20M', '20M-25M', '>25M'])
price_range_counts = price_ranges.value_counts().sort_index()

plt.figure(figsize=(8, 6))
price_range_counts.plot(kind='bar')
plt.title('Price Range Distribution')
plt.xlabel('Price Range (Rp)')
plt.ylabel('Frequency')
plt.show()

# 7. Rating Analysis
rating_counts = data['Rating'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
rating_counts.plot(kind='bar')
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# 8. Brand Analysis
data['Brand'] = data['Product Name'].str.split().str[0]
brand_ratings = data.groupby('Brand')['Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
brand_ratings.plot(kind='bar')
plt.title('Average Rating by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()
