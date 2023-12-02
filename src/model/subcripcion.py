from config.db import db, app, ma

class Subcripcion(db.Model):
    __tablename__ = "tblsubcripciones"

    id = db.Column(db.Integer, primary_key=True)
    subcripcion_id = db.Column(db.Integer)
    subcripcion_name = db.Column(db.String(200))
    cant_pantallas = db.Column(db.Integer)
    date_start = db.Column(db.DateTime) 
    

    def __init__(self,subcripcion_id,subcripcion_name,cant_pantallas,date_start):
        self.subcripcion_id = subcripcion_id
        self.subcripcion_name = subcripcion_name
        self.cant_pantallas = cant_pantallas
        self.date_start = date_start
        

with app.app_context():
     db.create_all()

class SubcripcionSchema(ma.Schema):
    class Meta:
        fields = ('subcripcion_id', 'subcripcion_name', 'cant_pantallas', 'date_start')