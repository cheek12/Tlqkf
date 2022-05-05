from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from pybo import db
from pybo.models import Question,Answer
from ..forms import AnswerForm

bp = Blueprint('answer', __name__ , url_prefix = '/answer') # answer_view.py가 answer이라는 이름의 bp파일임을 나타냄

@bp.route('/create/<int:question_id>', methods = ('POST',)) #답변 저장 템플릿에 있는 form 요소의 method값과 일치해야
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content'] #name속성이 'content'인 값
        answer = Answer(content = content, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail',question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)