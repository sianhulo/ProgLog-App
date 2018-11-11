from app.handlers import db

subjects_approved = db.Table('user_subjects_approved',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.id'), primary_key=True)
)


class Base(db.Model):
    __abstract__ = True

    id            = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date_created  = db.Column(db.DateTime, default  = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default  = db.func.current_timestamp(),
                                           onupdate = db.func.current_timestamp())

class User(Base):
    __tablename__ = 'users'

    name     = db.Column(db.String(150), nullable = False)
    email    = db.Column(db.String(250), nullable = False,
                                         unique   = True)
    password = db.Column(db.String(250), nullable = False)
    approved = db.relationship('Subject', 
                               secondary = subjects_approved,
                               lazy      = 'subquery',
                               backref   = db.backref('users', lazy = True))
    
    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.email)
