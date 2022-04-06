from pybo import db

class Question(db.Model): #db.Model클래스 상속
    id = db.Column(db.Integer, primary_key=True) # (속성의 데이터 타입 지정, 속성을 기본 키로 지정)
    subject = db.Column(db.String(200), nullable=False) # nullable=False 속성에 빈값 허용 X
    content = db.Column(db.Text(), nullable= False)
    create_date = db.Column(db.DateTime(), nullable= False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))# 쿼리 이용해서 질문 삭제하면 같이 삭제됨
    question = db.relationship('Question', backref=db.backref('answer_set',)) #(참조할 모델, 역참조할 모델)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
