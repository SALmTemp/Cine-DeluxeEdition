from config.db import db, app, ma

class User(db.Model):
    __tablename__ = "tblusers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    id_subcripcion = db.Column(db.Integer, db.ForeignKey('tblsubcripciones.subcripcion_id'))
    id_cuenta = db.Column(db.Integer, db.ForeignKey('tblcuentas.cuenta_id'))
    id_estado = db.Column(db.Integer, db.ForeignKey('tblestados.estado_id'))
    id_experiencia = db.Column(db.Integer, db.ForeignKey('tblexperiencias.experiencia_id'))
    id_perfilescreados = db.Column(db.Integer, db.ForeignKey('tblperfilescreados.perfilescreados_id'))
    id_usersroles = db.Column(db.Integer, db.ForeignKey('tblusersroles.rol_id'))
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    registration = db.Column(db.String(50))
    

    def __init__(self,id, id_subcripcion, id_cuenta, id_estado,id_experiencia,id_perfilescreados,id_usersroles,username,email,password,fullname,registration):
        self.id= id
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

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','id_subcripcion', 'id_cuenta', 'id_estado', 'id_experiencia', 'id_perfilescreados','id_usersroles','username','email','password','fullname','registration')