from flask import Blueprint , render_template, request, url_for
from ..models import Question
from ..forms import QuestionForm, AnswerForm
from datetime import datetime
from werkzeug.utils import redirect
from .. import db



bp = Blueprint('question',__name__,url_prefix='/question')
@bp.route('/list')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())  # order_by : 조회 결과 출력 Question.create_date.desc() : 작성일시 기준 역순으로
    # question_list = Question.query.order_by(Question.create_date.asc()) 작성일시 순서로 정렬
    return render_template('question/question_list.html',question_list=question_list)  # render_template 템플릿 파일 화면에 보여줌

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id) # get_or_404 : 해당 데이터 찾을 수 없으면 404페이지 출력
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/' , methods=('GET','POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))


    return render_template('question/question_form.html', form=form)
