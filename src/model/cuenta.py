from config.db import db, app, ma

class Cuentas(db.Model):
    __tablename__ = "tblcuentas"

    cuenta_id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Double)
    descripcion = db.Column(db.Text)
    

    def __init__(self,cuenta_id, saldo,descripcion):
        self.cuenta_id= cuenta_id
        self.saldo = saldo
        self.descripcion = descripcion
        

        with app.app_context():
            db.create_all()

class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('cuenta_id','saldo', 'descripcion')