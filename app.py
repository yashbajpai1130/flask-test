from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    return render_template('submit.html', input_text=user_input)

if __name__ == '__main__':
    serve(app, port = "5000")