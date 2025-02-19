from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


if __name__ == '__main__':
    app.run()
