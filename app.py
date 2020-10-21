from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'any_random_characters'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from models import User, Question, Answer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    questions_dict = Question.query.all()
    return render_template('index.html', questions_dict=questions_dict)


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

@app.route('/Register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
