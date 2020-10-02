from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'QnA App | Homepage'

@app.route('/Ask a question')
def ask():
    return 'QnA App  |  Ask a question'

@app.route('Ask a question')
def view():
    return 'QnA App  |  View a question'

if __name__ == "__main__":
    app.run(debug = True)