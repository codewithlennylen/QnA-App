from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user



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


@app.route('/about')
def about():
    return render_template('aboutt.html')


@app.route('/askaquestion')
def ask():
    return render_template('ask.html')

@app.route('/viewaquestion')
def view():
    return render_template('view.html')

@app.route('/register', methods=['GET','POST'])
def register():
    # If we get a POST Request, Proceed to Registration
    if request.method == 'POST':
        # Get the Data from the Register Form
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        # Check if the username exists in the database
        user_exists = User.query.filter_by(username=username).all()
        if user_exists:
            error_msg = 'That username already exists. Please use a different one.'
            return render_template('register.html',error_msg=error_msg)

        # Check if the password matcheds with the confirm password
        if password != confirmPassword:
            error_msg = 'The Passwords do not match. Please Try Again.'
            return render_template('register.html',error_msg=error_msg)


        # if all checks have passed, proceed to add the user to the datbase.
        new_user = User(
            username=username,
            password=password,
            is_admin=False,
            is_expert=False
        )
        db.session.add(new_user)
        db.session.commit()

        # Redirect the new user to the Login Page
        return redirect(url_for('login'))

    # Else if this is a GET request, show the register page
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            # Since the user exists let's proceed to check whether the password is correct
            if password == user_exists.password:
                # Passwords match! > Proceed to the homepage
                login_user(user_exists)
                return redirect(url_for('index'))
                
            # Else if the passwords don't match > Inform the user to try again
            else:
                error_msg = 'The Username or Password is wrong. Please try again!'
                return render_template('login.html', error_msg=error_msg)
        # Else if the user does not exist in the database, Inform them to register
        else:
            error_msg = 'The Username Does not Exist. Register Instead?'
            return render_template('login.html', error_msg=error_msg)
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
