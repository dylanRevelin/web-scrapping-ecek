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
        data_info, data_desc, mean_price, median_price, mean_rating, median_rating = analyze_data(filename)
        return redirect(url_for('results', 
                                filename=filename, 
                                data_info=data_info, 
                                data_desc=data_desc, 
                                mean_price=mean_price, 
                                median_price=median_price, 
                                mean_rating=mean_rating, 
                                median_rating=median_rating))

@app.route('/results/<filename>')
def results(filename):
    data = pd.read_excel(filename)
    return render_template('results.html', 
                            data=data, 
                            data_info=request.args.get('data_info'), 
                            data_desc=request.args.get('data_desc'), 
                            mean_price=request.args.get('mean_price'), 
                            median_price=request.args.get('median_price'), 
                            mean_rating=request.args.get('mean_rating'), 
                            median_rating=request.args.get('median_rating'))

if __name__ == "__main__":
    app.run(debug=True)
