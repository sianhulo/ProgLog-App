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

mod_tests = Blueprint('tests',
                      __name__,
                      url_prefix='/tests')

@mod_tests.route('/', methods=['GET'])
def home():
    return 'Hey! :)', 200
