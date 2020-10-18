from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Integer, nullable=True)
    is_expert = db.Column(db.Integer, nullable=True)

    # define relationships 
    questions_asked = db.relationship(
        'Question',
        foreign_keys='Question.asked_by_id',
        backref='asker',
        lazy=True
    )

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_text = db.Column(db.Text, nullable = False)
    category = db.Column(db.String(20), nullable = False)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # define relationships
    answers_to_question = db.relationship(
        'Answer',
        foreign_keys = 'Answer.for_question_id',
        backref='the_question',
        lazy=True
    )

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.Text, nullable=False)
    for_question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
