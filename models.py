from app import db



class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_text = db.Column(db.Text, nullable = False)
    category = db.Column(db.String(20), nullable = False)
    answer = db.Column(db.Text, nullable=True)