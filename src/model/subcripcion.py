from config.db import db, app, ma
from datetime import datetime, timezone, timedelta

class Subcripcion(db.Model):
    __tablename__ = "tblsubcripciones"

    id = db.Column(db.Integer, primary_key=True)
    subcripcion_name = db.Column(db.String(200))
    cant_pantallas = db.Column(db.Integer)
    saldo = db.Column(db.DECIMAL(precision=10,scale=2))
    date_start = db.Column(db.DateTime, default=None)
    

    def __init__(self, subcripcion_name, cant_pantallas, saldo, date_start=None):
        self.subcripcion_name = subcripcion_name
        self.cant_pantallas = cant_pantallas
        self.saldo = saldo
        self.date_start = date_start
        

with app.app_context():
    db.create_all()

    # Verificar si ya hay registros en la tabla
    if Subcripcion.query.count() == 0:
        times = datetime.now()
        # Crear registros de suscripciones
        subcripcion1 = Subcripcion('basic', 1, float(1), times)
        subcripcion2 = Subcripcion('Trial', 1, float(1), times)
        subcripcion3 = Subcripcion('Personal', 1, float(1), times)
        subcripcion4 = Subcripcion('duo', 2, float(2), times)
        
        db.session.add_all([subcripcion1, subcripcion2, subcripcion3, subcripcion4])
        db.session.commit()

class SubcripcionSchema(ma.Schema):
    class Meta:
        fields = ( 'subcripcion_name', 'cant_pantallas', 'saldo', 'date_start' )
