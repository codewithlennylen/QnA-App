from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myquestions')
def myquestions():
    return render_template('myquestions.html')

@app.route('/login')
def login():
    return 'QnA App | Login Here'

@app.route('/about')
def about():
    return 'QnA App | About.'

@app.route('/Askaquestion')
def ask():
    return 'QnA App  |  Ask a question'

@app.route('/Viewaquestion')
def view():
    return 'QnA App  |  View a question'


if __name__ == "__main__":
    app.run(debug = True)
