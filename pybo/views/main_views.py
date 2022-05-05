from flask import Blueprint , url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/fuckyou')
def fuck_you():
    return 'fuck you!'

@bp.route('/')
def index():
    return redirect(url_for('question._list')) #url_for() 설정된 함수명으로 url을 역으로 찾아줌, question_views의 _list()


