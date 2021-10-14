

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
    cursor.execute("SELECT * FROM products limit 4")
    # AFter executing the query above, get all rows
    deals = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    # AFter executing the query above, get all rows
    brands = cursor.fetchall()

    return render_template('index.html', deals=deals)

# 1. starts here
@app.route('/topdeals')
def index():
    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_brand FROM products")
    brands = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_category FROM products")
    categories = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT color FROM products")
    colors = cur.fetchall()
    # 2. goes to top deals html
    return render_template('topdeals.html', brands=brands, categories=categories, colors = colors)


# 5. fetches all the products and returns a json array
@app.route("/fetchrecords1",methods=["POST","GET"])
def fetchrecords1():
    cur = connection.cursor()
    if request.method == 'POST':
        # category
        name = request.form['insert_string']
        my_result = tuple(map(str, name.split(',')))

        # brand
        name2 = request.form['insert_string2']
        my_result2 = tuple(map(str, name2.split(',')))

        # discount
        name3 = request.form['insert_string3']
        my_result3 = tuple(map(str, name3.split(',')))

        print(my_result)
        print(my_result2)
        print(my_result3)

        if len(name) == 0 and len(name2) == 0 and len(name3) == 0:
            print('here')
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_cost ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print(productlist)
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and not my_result2[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand IN %s",
                [my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and  my_result2[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s",
                [my_result,my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result3[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and color IN %s",
                [my_result, my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result2[0] and  my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        #categories
        elif my_result2[0] and not my_result[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category IN %s",
                [my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result2[0] and  my_result[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category  IN %s and product_brand IN %s",
                [my_result2,my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result2[0] and  my_result3[0] and not my_result[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category IN %s and color IN %s",
                [my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result2[0] and  my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        #color
        elif my_result3[0] and not my_result[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s",
                [my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s and product_brand IN %s",
                [my_result3, my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result2[0] and not my_result[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s and product_category  IN %s",
                [my_result3, my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result2[0] and my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2, my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})
        else:
            cur.execute("SELECT * FROM products  ORDER BY product_id ASC")
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

    else:
        cur.execute("SELECT * FROM products ORDER BY product_id ASC")
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


from werkzeug.security import generate_password_hash, check_password_hash
# shopping Cart
@app.route('/add', methods=['POST'])
def add_product_to_cart():
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        # validate the received values
        if _quantity and _code and request.method == 'POST':
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM products WHERE product_id= %s", _code)
            row = cursor.fetchone()

            itemArray = {row['product_id']: {'product_name': row['product_name'], 'product_id': row['product_id'], 'quantity': _quantity, 'product_cost': row['product_cost'],
                              'image_url': row['image_url'], 'total_price': _quantity * row['product_cost'],
                                             'product_brand': row['product_brand']}}
            print(type(itemArray))

            all_total_price = 0
            all_total_quantity = 0
            session.modified = True
            if 'cart_item' in session:
                if row['product_id'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row['product_id'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['product_cost']

                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)


                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price

            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row['product_cost']



            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(url_for('.cart'))
        else:
            return 'Error while adding item to cart'



@app.route('/cart')
def cart():
    return render_template('cart.html')



@app.route('/empty')
def empty_cart():
    try:
        if 'cart_item' in session or 'all_total_quantity' in session or 'all_total_price' in session:
            session.pop('cart_item', None)
            session.pop('all_total_quantity', None)
            session.pop('all_total_price', None)
            return redirect(url_for('.cart'))
        else:
            return redirect(url_for('.cart'))

    except Exception as e:
        print(e)



@app.route('/delete/<string:code>')
def delete_product(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        # return redirect('/')
        return redirect(url_for('.cart'))
    except Exception as e:
        print(e)


def array_merge( first_array , second_array ):
     if isinstance( first_array , list) and isinstance( second_array , list ):
      return first_array + second_array
     elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
      return dict( list( first_array.items() ) + list( second_array.items() ) )
     elif isinstance( first_array , set ) and isinstance( second_array , set ):
      return first_array.union( second_array )
     return False




if __name__ == '__main__':
    app.run(debug=True)