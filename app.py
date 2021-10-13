

from flask import *
# create a flask application

app = Flask(__name__)
app.secret_key = 'A+4#s_T%P8g0@o?6'

import pymysql
connection = pymysql.connect(host='localhost', user='root',password='',
                                 database='ecom')



@app.route('/')
def home():
    # Connect to database
    # Create a cursor to execute SQL Query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE top_deal = 'Yes' ")
    # AFter executing the query above, get all rows
    deals = cursor.fetchall()

    cursor.execute("SELECT * FROM products WHERE top_brand = 'Yes' ")
    # AFter executing the query above, get all rows
    brands = cursor.fetchall()


    return render_template('index.html', deals=deals)

# 1. starts here
@app.route('/topdeals')
def index():
    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_brand FROM products Where top_deal = 'Yes'")
    brands = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_category FROM products Where top_deal = 'Yes'")
    categories = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT color FROM products Where top_deal = 'Yes'")
    colors = cur.fetchall()
    # 2. goes to top deals html
    return render_template('topdeals.html', brands=brands, categories=categories, colors = colors)


# 5. fetches all the products and returns a json array
@app.route("/fetchrecords1",methods=["POST","GET"])
def fetchrecords1():
    cur = connection.cursor()
    if request.method == 'POST':
        pass

    else:
        cur.execute("SELECT * FROM products Where top_deal = 'Yes' ORDER BY product_id ASC")
        productlist = cur.fetchall()
        # this json response productlist mapped to  response.html
        return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

@app.route('/single/<product_id>')
def single(product_id):

            # Connect to database
            connection = pymysql.connect(host='localhost', user='root', password='',
                                         database='ecom')

            # Create a cursor to execute SQL Query
            cursor = connection.cursor()
            #below %s is a placeholder o make sure that the id is actually detected
            cursor.execute('SELECT * FROM products WHERE product_id= %s ', (product_id))
            # AFter executing the query above, to get one row
            row = cursor.fetchone()

            # after getting the row forward it to single.html for users to access it
            return render_template('single.html', row=row)










if __name__ == '__main__':
    app.run(debug=True)