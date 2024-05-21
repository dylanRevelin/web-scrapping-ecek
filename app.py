from flask import Flask, render_template, request, redirect, url_for, session, make_response
from scraping import scrape_products
from analysis import analyze_data
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session management

@app.template_filter('format_price')
def format_price(price):
    return "Rp {:,.0f}".format(price)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        product_name = request.form['product_name']
        pages = int(request.form['pages'])
        filename = scrape_products(product_name, pages)
        data_sorted_price, mean_price, median_price, mean_rating, median_rating = analyze_data(filename)
        
        # Store results and product name in session
        session['product_name'] = product_name
        session['data_sorted_price'] = data_sorted_price.to_dict(orient='records')
        session['mean_price'] = mean_price
        session['median_price'] = median_price
        session['mean_rating'] = mean_rating
        session['median_rating'] = median_rating
        
        return redirect(url_for('results', filename=filename))

@app.route('/results')
def results():
    # Retrieve results from session
    product_name = session.get('product_name')
    data_sorted_price = session.get('data_sorted_price')
    mean_price = session.get('mean_price')
    median_price = session.get('median_price')
    mean_rating = session.get('mean_rating')
    median_rating = session.get('median_rating')
    
    return render_template('results.html', 
                           product_name=product_name,
                           data=data_sorted_price, 
                           mean_price=mean_price,
                           median_price=median_price,
                           mean_rating=mean_rating,
                           median_rating=median_rating)

@app.route('/download-results')
def download_results():
    # Retrieve the scraped data from the session
    data_sorted_price = session.get('data_sorted_price')
    mean_price = session.get('mean_price')
    median_price = session.get('median_price')
    mean_rating = session.get('mean_rating')
    median_rating = session.get('median_rating')

    # Create a DataFrame from the data
    df = pd.DataFrame(data_sorted_price)

    # Create an in-memory Excel file
    excel_data = BytesIO()
    with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Results')
        workbook = writer.book
        worksheet = writer.sheets['Results']
        # Optionally, add mean and median statistics to the Excel file
        worksheet.write(len(df) + 2, 0, 'Mean Price:')
        worksheet.write(len(df) + 2, 1, mean_price)
        worksheet.write(len(df) + 3, 0, 'Median Price:')
        worksheet.write(len(df) + 3, 1, median_price)
        worksheet.write(len(df) + 4, 0, 'Mean Rating:')
        worksheet.write(len(df) + 4, 1, mean_rating)
        worksheet.write(len(df) + 5, 0, 'Median Rating:')
        worksheet.write(len(df) + 5, 1, median_rating)
    excel_data.seek(0)

    # Create a response object
    response = make_response(excel_data.getvalue())

    # Set headers to trigger file download
    response.headers['Content-Disposition'] = 'attachment; filename=scraped_data.xlsx'
    response.headers['Content-type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    return response

if __name__ == "__main__":
    app.run(debug=True)
