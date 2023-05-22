data = [{"titles": "Grocery", "images": "https://rukminim1.flixcart.com/flap/128/128/image/29327f40e9c4d26b.png?q=100"}, {"titles": "Mobiles", "images": "https://rukminim1.flixcart.com/flap/128/128/image/22fddf3c7da4c4f4.png?q=100"}, {"titles": "Fashion", "images": "https://rukminim1.flixcart.com/fk-p-flap/128/128/image/0d75b34f7d8fbcb3.png?q=100"}, {"titles": "Electronics", "images": "https://rukminim1.flixcart.com/flap/128/128/image/69c6589653afdb9a.png?q=100"}, {"titles": "Home", "images": "https://rukminim1.flixcart.com/flap/128/128/image/ab7e2b022a4587dd.jpg?q=100"}, {"titles": "Appliances", "images": "https://rukminim1.flixcart.com/flap/128/128/image/0ff199d1bd27eb98.png?q=100"}, {"titles": "Travel", "images": "https://rukminim1.flixcart.com/flap/128/128/image/71050627a56b4693.png?q=100"}, {"titles": "Top Offers", "images": "https://rukminim1.flixcart.com/flap/128/128/image/f15c02bfeb02d15d.png?q=100"}, {"titles": "Beauty, Toys & More", "images": "https://rukminim1.flixcart.com/flap/128/128/image/dff3f7adcf3a90c6.png?q=100"}, {"titles": "Two Wheelers", "images": "https://rukminim1.flixcart.com/fk-p-flap/128/128/image/05d708653beff580.png?q=100"}]
import requests
from flask import Flask,jsonify,request


app = Flask(__name__)

@app.route("/")
def n_data():
    return jsonify(data)

@app.route("/add",methods = ["POST"])
def post_data():
    query = request.get_json()
    data.append(query)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug = True)
