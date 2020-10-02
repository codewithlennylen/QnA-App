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

@app.route('/Askaquestion')
def ask():
    return 'QnA App  |  Ask a question'

@app.route('/Viewaquestion')
def view():
    return 'QnA App  |  View a question'


if __name__ == "__main__":
    app.run(debug = True)
