from config.db import db, app, ma

class PerfilesCreados(db.Model):
    __tablename__ = "tblperfilescreados"

    id_perfilescreados = db.Column(db.Integer, primary_key=True)
    id_token = db.Column(db.Integer, db.ForeignKey('tbltoken.id_token'))
    nombre = db.Column(db.String(200))
    imagen = db.Column(db.String(200))
    fecha_nacimiento = db.Column(db.Date) 
    

    def __init__(self,id_token,nombre,imagen,fecha_nacimiento):
        self.id_token = id_token
        self.nombre = nombre
        self.imagen = imagen
        self.fecha_nacimiento = fecha_nacimiento
        

with app.app_context():
    db.create_all()

class PerfilesCreadosSchema(ma.Schema):
    class Meta:
        fields = ('id_token', 'nombre', 'imagen', 'fecha_nacimiento')