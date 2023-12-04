from config.db import db, app, ma
from sqlalchemy import Numeric

class Cuentas(db.Model):
    __tablename__ = "tblcuentas"

    cuenta_id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(Numeric(precision=18, scale=2))  # Ajusta precision y scale según tus necesidades
    descripcion = db.Column(db.Text)
    

    def __init__(self, saldo, descripcion):
        self.saldo = saldo
        self.descripcion = descripcion

with app.app_context():
    db.create_all()

    # Verificar si ya hay registros en la tabla
    if Cuentas.query.count() == 0:
        # Crear registros de cuentas
        cuenta1 = Cuentas(0.0, 'Cuenta Ahorros')  # Puedes ajustar el saldo según tus necesidades
        cuenta2 = Cuentas(0.0, 'Cuenta Corriente')
        cuenta3 = Cuentas(0.0, 'Cuenta Chequera')
        cuenta4 = Cuentas(0.0, 'Cuenta Nomina')
        
        db.session.add_all([cuenta1, cuenta2, cuenta3, cuenta4])
        db.session.commit()

class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('saldo', 'descripcion')
