from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject=StringField('제목',validators=[DataRequired('제목은 필수 입력 항목입니다')]) # <input type='text'>에 대응하는 자료형, (라벨,필드값 검증)
    content=TextAreaField('내용',validators=[DataRequired('내용은 필수 입력 항목입니다')]) # <textarea>에 대응하는 자료형

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다')])