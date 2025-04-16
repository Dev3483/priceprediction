from flask import Flask, render_template, request, redirect, jsonify
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations': util.get_location_names() # Replace with actual location names
    })  
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    bath = float(request.form['bath'])
    bhk = float(request.form['bhk'])
    location = request.form['location']
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run(debug=True)