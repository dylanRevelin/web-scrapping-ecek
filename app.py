from flask import Flask, render_template, request, redirect, url_for
from scraping import scrape_products
from analysis import analyze_data
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        product_name = request.form['product_name']
        pages = int(request.form['pages'])
        filename = scrape_products(product_name, pages)
        data_sorted_price, data_sorted_rating, mean_price, median_price, mean_rating, median_rating = analyze_data(filename)
        return redirect(url_for('results', 
                                filename=filename, 
                                data_sorted_price=data_sorted_price, 
                                data_sorted_rating=data_sorted_rating, 
                                mean_price=mean_price, 
                                median_price=median_price, 
                                mean_rating=mean_rating, 
                                median_rating=median_rating))



@app.route('/results/<filename>')
def results(filename):
    data_sorted_price, mean_price, median_price, mean_rating, median_rating = analyze_data(filename)
    return render_template('results.html', 
                            data=data_sorted_price, 
                            mean_price=mean_price,
                            median_price=median_price,
                            mean_rating=mean_rating,
                            median_rating=median_rating,)


if __name__ == "__main__":
    app.run(debug=True)
