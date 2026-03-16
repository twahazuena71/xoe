from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///school.db'
app.config['SECRET_KEY']='$hhhhyhg%89897'
db=SQLAlchemy(app)
class student(db.Model):
    pers_id=db.Column(db.Integer,primary_key=True)
    pers_name=db.Column(db.String(20))
    pers_age=db.Column(db.Integer)
    pers_password=db.Column(db.String)
class StudentRegisterForm(FlaskForm):
    student_name=StringField('pers_name',validators=[InputRequried()Length(min=5,max=15)])
    student_age=IntegerField('pers_age',validators=[InputRequired])
    with app.app_context():
   db.create_all()
@app.route('/')
def index():
    return 'welcome to python'
if __name__=='_main_':
    app.run(debug=True)