from itertools import product
from flask import Flask, render_template, jsonify, request
from flask import Response, redirect, url_for
import database as dbase
from products import Products
from flask_cors import CORS

app = Flask(__name__)
db=dbase.dbConnection()
CORS(app)

#home
@app.route('/')
def home():
    return render_template('index.html')


#Metodo GET
@app.route('/get-products', methods=['GET'])

def getproducts():
    products=db['products']
    productsReceived=products.find()
    response =[]
    for i in productsReceived:
        response.append(str(i))
        return jsonify(response)
    

#Errores
@app.errorhandler(404)
def notFound(error=None):
    message={
        'message':'No encontrado' + request.url,
        'status':'404 not found'
    }
    response=jsonify(message)
    response.status.code=404
    response.headers.add('Acces-control_Allow-Origin', '*')
    return response

if __name__=="__main__":
    app.run(debug=False, port=4000)