from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login/login.html')

@app.route('/home')
def inicio():
    return render_template('home/home.html')

@app.route('/category')
def inicio():
    return render_template('category/category.html')

@app.route('/details')
def inicio():
    return render_template('details/details.html')

@app.route('/elements')
def inicio():
    return render_template('elements/elements.html')

@app.route('/product_details')
def inicio():
    return render_template('product_details/product_details.html')

@app.route('/signin')
def inicio():
    return render_template('signin/signin.html')


if __name__ =='__main__':
    app.run(debug=True)