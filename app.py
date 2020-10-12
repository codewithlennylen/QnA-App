from flask import Flask, render_template, url_for

app = Flask(__name__)

questions = {
    "How do you restart a computer?": ["Networking","Random Answer"],
    "What programming language should i learn": ["Computer programming"],
    "What is linux": ["Computing","Random Answer"],
    "Is pirate-bay illegal": ["Computer software"],
    "The blue screen of death!": ["Computer software","Random Answer"],
    "What is linux?": ["Computing","Random Answer"],
    "How do you restart a computer??": ["Computer software"],
    "How do you access the dark web?": ["Networking","Random Answer"],
    "Which is the best VPN to use?": ["Security"],
    "How do I know if my computer has been hacked?": ["Security"],
    "Which is the best arcade game to download now?": ["Gaming"],
    "Which application can i download to use in listening mp3 music?": ["Application","Random Answer"]
}


@app.route('/')
def index():
    return render_template('index.html', questions_dict=questions)


@app.route('/myquestions')
def myquestions():
    return render_template('myquestions.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('aboutt.html')


@app.route('/Askaquestion')
def ask():
    return render_template('ask.html')


@app.route('/Viewaquestion')
def view():
    return render_template('view.html')


if __name__ == "__main__":
    app.run(debug=True)
