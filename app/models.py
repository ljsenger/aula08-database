from app import db

class Usuario(db.Model):
    __tablename__='usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(64), index=True, unique=True)
    email   = db.Column(db.String(120), index=True, unique=True)
    senha   = db.Column(db.String(128))
    endereco = db.Column(db.String(128))
    funcao_id = db.Column(db.Integer, db.ForeignKey('funcao.id'))
    
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.usuario)  

class Funcao(db.Model):
    __tablename__='funcao'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), index=True, unique=True)
    usuario = db.relationship('Usuario', backref='funcao', lazy='dynamic')

    def __repr__(self):
        return '<Funcao {}>'.format(self.descricao)  

