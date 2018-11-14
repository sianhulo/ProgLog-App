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
from werkzeug import (
    generate_password_hash,
    check_password_hash
)
from app.mod_auth.forms import (
    LoginForm,
    SignupForm
)
from app.handlers import db
from app.mod_auth.models import User
from sqlalchemy.exc import IntegrityError

mod_auth = Blueprint('auth', 
                     __name__, 
                     url_prefix='/auth')

@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Bienvenido, %s' % user.name)
            return redirect(url_for('tests.dashboard'))
        flash('Email o contraseña incorrectos.', 'error')
    
    return render_template('auth/signin.html', form=form)

@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        user = User(email    = form.email.data,
                    name     = form.name.data,
                    password = generate_password_hash(form.password.data))
        try:
            db.session.add(user)
            db.session.commit()

            # Since we are redirecting to the signin page
            # we don't need to save the session.
            # session['user_id'] = user.id
            flash('Usuario creado con éxito. :)')

            return redirect(url_for('auth.signin'))
        except IntegrityError as ie:
            db.session.rollback()
            flash(str(ie))
        except Exception as e:
            db.session.rollback()
            flash(str(e))

    return render_template('auth/signup.html', form=form)
