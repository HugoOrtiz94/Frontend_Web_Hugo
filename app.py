from flask import Flask
from flask import render_template
from PIL import Image

app=Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def inicio():
    return render_template('login/login.html')

@app.route('/home')
def inicio_home():
    return render_template('home/home.html')

@app.route('/category')
def inicio_category():
    return render_template('category/category.html')

@app.route('/details')
def inicio_details():
    return render_template('details/details.html')

@app.route('/elements')
def inicio_elements():
    return render_template('elements/elements.html')

@app.route('/product_details')
def inicio_product_details():
    return render_template('product_details/product_details.html')

@app.route('/signin')
def inicio_signin():
    return render_template('signin/signin.html')

if __name__ =='__main__':
    app.run(debug=True)
    
# Configurar Pillow para manejar imágenes PNG
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)