from config.db import db, app, ma
from datetime import date


class PerfilesCreados(db.Model):
    __tablename__ = "tblperfilescreados"

    id_perfilescreados = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    
# Verificar si ya hay registros en la tabla
    # Verificar si ya hay registros en la tabla
    if PerfilesCreados.query.count() == 0:
        # Crear registros de perfiles creados
        perfil1 = PerfilesCreados(id_token=1, nombre='test', imagen='https://www.google.com/url?sa=i&url=https%3A%2F%2Fdribbble.com%2Fshots%2F2495400-Horror-Movie-Characters-Billy-The-Puppet&psig=AOvVaw3nW5NBvmiXQtEwKs1SBn_b&ust=1702017694496000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPDvlZPc_IIDFQAAAAAdAAAAABAf', fecha_nacimiento=date(1990, 5, 15))
        perfil2 = PerfilesCreados(id_token=2, nombre='testoperador', imagen='https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Far%2Fimages%2Foperator-icon-glowing-sign-logo-vector%2F356647241&psig=AOvVaw2QCvgYwwq3HyF6niNAtvQY&ust=1702020637766000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLDtrY3n_IIDFQAAAAAdAAAAABAF', fecha_nacimiento=date(1990, 5, 16))
        db.session.add_all([perfil1, perfil2])
        db.session.commit()

class PerfilesCreadosSchema(ma.Schema):
    class Meta:
        fields = ('id_token', 'nombre', 'imagen', 'fecha_nacimiento')