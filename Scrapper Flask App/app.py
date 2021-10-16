from flask import Flask, request
from werkzeug.wrappers import response
from Scrappers import amazon, flipkart
import json

app = Flask(__name__)


@app.route("/amazon_products", methods=['POST'])
def amazon_products():
    req = request.get_json(force=True)
    all_products = amazon.amazon_products(req['search'])
    if all_products and all_products['type'] == 'success':
        all_products['products'] = enumerate(all_products['products'])
    
    response = app.response_class(
        response = json.dumps(all_products),
        status=200,
        mimetype='application/json'
    ) 
    return response


@app.route("/flipkart_products", methods=['POST'])
def flipkart_products():
    req = request.get_json(force=True)
    all_products = flipkart.flipkart_products(req['search'])
    if all_products and all_products['type'] == 'success':
        all_products['products'] = enumerate(all_products['products'])
    
    response = app.response_class(
        response = json.dumps(all_products),
        status=200,
        mimetype='application/json'
    ) 
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
