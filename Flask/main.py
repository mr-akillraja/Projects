from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    input_id = request.form['passenger_id']

    data = pd.read_csv("input.csv")

    passenger = data[data['ASSET ID'] == input_id]

    return render_template('result.html', passenger=passenger)

if __name__ == '__main__':
    app.run(debug=True)
