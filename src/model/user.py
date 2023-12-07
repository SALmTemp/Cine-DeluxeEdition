from config.db import db, app, ma
from datetime import datetime, timedelta

class User(db.Model):
    __tablename__ = "tblusers"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    id_subcripcion = db.Column(db.Integer, db.ForeignKey('tblsubcripciones.id'))
    id_cuenta = db.Column(db.Integer, db.ForeignKey('tblcuentas.cuenta_id'))
    id_estado = db.Column(db.Integer, db.ForeignKey('tblestados.estado_id'))
    id_experiencia = db.Column(db.Integer, db.ForeignKey('tblexperiencias.experiencia_id'))
    id_perfilescreados = db.Column(db.Integer, db.ForeignKey('tblperfilescreados.id_perfilescreados'))
    id_usersroles = db.Column(db.Integer, db.ForeignKey('tblusersroles.rol_id'))
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    fullname = db.Column(db.String(200))
    registration = db.Column(db.DateTime) 
    

    def __init__(self,id_subcripcion, id_cuenta, id_estado,id_experiencia,id_perfilescreados,id_usersroles,username,email,password,fullname,registration):
        self.id_subcripcion = id_subcripcion
        self.id_cuenta = id_cuenta
        self.id_estado = id_estado
        self.id_experiencia = id_experiencia
        self.id_perfilescreados = id_perfilescreados
        self.id_usersroles = id_usersroles
        self.username = username
        self.email = email
        self.password = password
        self.fullname = fullname
        self.registration = registration
        

with app.app_context():
    db.create_all()

# Verificar si ya hay registros en la tabla
    if User.query.count() == 0:
        # Crear registros de usuarios
        user1 = User(
            id_subcripcion=1,
            id_cuenta=1,
            id_estado=1,
            id_experiencia=1,
            id_perfilescreados=1,
            id_usersroles=1,
            username='SALM',
            email='null',
            password='SALMñ',
            fullname='SALM',
            registration=datetime.now()
        )
        user2 = User(
            id_subcripcion=2,
            id_cuenta=2,
            id_estado=2,
            id_experiencia=2,
            id_perfilescreados=2,
            id_usersroles=2,
            username='operador_salm',
            email='stremovify@gmail.com',
            password='Operadorñ',
            fullname='Operador',
            registration=datetime.now()
        )
        
        db.session.add_all([user1, user2])
        db.session.commit()
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id_subcripcion', 'id_cuenta', 'id_estado', 'id_experiencia', 'id_perfilescreados','id_usersroles','username','email','password','fullname','registration')