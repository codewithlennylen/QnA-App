from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'QnA App | Homepage'

@app.route('/myquestions')
def myquestions():
    return 'QnA App | My Questions'

@app.route('/login')
def login():
    return 'QnA App | Login Here'

@app.route('/about')
def about():
    return 'QnA App | About.'


if __name__ == "__main__":
    app.run(debug = True)