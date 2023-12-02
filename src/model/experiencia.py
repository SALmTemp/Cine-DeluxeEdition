from config.db import db, app, ma

class Experiencia(db.Model):
    __tablename__ = "tblexperiencias"

    experiencia_id = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.Integer)
    experiencia = db.Column(db.Integer)
    

    def __init__(self,experiencia_id, nivel,experiencia):
        self.experiencia_id= experiencia_id
        self.nivel = nivel
        self.experiencia = experiencia
        

        with app.app_context():
            db.create_all()

class ExperienciasSchema(ma.Schema):
    class Meta:
        fields = ('experiencia_id','nivel', 'experiencia')