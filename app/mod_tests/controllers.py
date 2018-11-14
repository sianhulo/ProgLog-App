from flask import (
    Blueprint, 
    request,
    render_template, 
    flash,
    g, 
    session,
    redirect,
    url_for
)
from app.mod_tests.models import (
    Type,
    Subject,
    Node
)
from app.mod_auth.models import User
from app.handlers import db
from app.mod_tests.helpers import get_node_file_path

mod_tests = Blueprint('tests',
                      __name__,
                      url_prefix='/tests')

@mod_tests.route('/dashboard', methods=['GET'])
def dashboard():
    subjects = Subject.query.order_by(Subject.id).all()

    return render_template('tests/test_dashboard.html', subjects = subjects)

@mod_tests.route('/<string:subject_name>', methods=['GET'], defaults={'node_id': 0})
@mod_tests.route('/<string:subject_name>/<int:node_id>', methods=['GET'])
def subject_test(subject_name, node_id):
    subject_name = subject_name.replace('+', ' ')
    subject = Subject.query.filter_by(name = subject_name).first()
    
    node = list(filter(lambda x: x.parent_node == node_id, subject.nodes))[0]
    node_file = open(get_node_file_path(subject_name, node.id), 'r')
    
    return render_template('tests/test.html', code = node_file.read())
