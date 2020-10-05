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
    return render_template('login.html')

@app.route('/about')
def aboutt():
    return render_template('aboutt.html')

@app.route('/Askaquestion')
def ask():
    return render_template('ask.html')

@app.route('/Viewaquestion')
def view():
    return render_template('view.html')


if __name__ == "__main__":
    app.run(debug = True)
