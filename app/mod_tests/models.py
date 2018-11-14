from app.handlers import db

class Base(db.Model):
    __abstract__ = True

    id            = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date_created  = db.Column(db.DateTime, default  = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default  = db.func.current_timestamp(),
                                           onupdate = db.func.current_timestamp())

class Type(Base):
    __tablename__ = 'types'

    name  = db.Column(db.String(100), nullable = False)
    nodes = db.relationship('Node',
                            lazy = 'select',
                            backref = db.backref('type', lazy='joined'))

    def __init__(self, type_name):
        self.name = type_name

    def __repr__(self):
        return '<Type %r>' % (self.name)

class Subject(Base):
    __tablename__ = 'subjects'

    name             = db.Column(db.String(120), nullable = False)
    prerequisite     = db.Column(db.Integer, nullable = False)
    minimum_approved = db.Column(db.Integer, nullable = False)
    nodes            = db.relationship('Node',
                                       lazy = 'select',
                                       backref = db.backref('subject', lazy = 'joined'))

    def __init__(self, name, prerequisite, minimum):
        self.name             = name
        self.prerequisite     = prerequisite
        self.minimum_approved = minimum

    def __repr__(self):
        return '<Subject %r>' % (self.name)

class Node(Base):
    __tablename__ = 'nodes'
    
    answer_parent = db.Column(db.String(250), nullable = False)
    parent_node   = db.Column(db.Integer, nullable = False)
    score         = db.Column(db.Integer, nullable = False)
    type_id       = db.Column(db.Integer, 
                              db.ForeignKey('types.id'),
                              nullable = False)
    subject_id    = db.Column(db.Integer, 
                              db.ForeignKey('subjects.id'),
                              nullable = False)

    def __init__(self, answer, parent, score):
        self.answer_parent = answer
        self.parent_node   = parent
        self.score         = score

    def __repr__(self):
        return '<Node %d>' % (self.id)
