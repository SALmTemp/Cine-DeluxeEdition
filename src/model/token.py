from config.db import db, app, ma
from datetime import datetime, timedelta

class Token(db.Model):
    __tablename__ = "tbltoken"

    id_token = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200))
    expiration = db.Column(db.DateTime)
    ip = db.Column(db.String(200)) 
    dispositivo = db.Column(db.String(200)) 

    def __init__(self, token, expiration, ip, dispositivo):
        self.token = token
        self.expiration = expiration
        self.ip = ip
        self.dispositivo = dispositivo

with app.app_context():
    db.create_all()

    # Verificar si ya hay registros en la tabla
    if Token.query.count() == 0:
        # Crear registros de tokens
        token1 = Token(
            token="token_1",
            expiration=datetime.now() + timedelta(days=1000),
            ip="null",
            dispositivo="Dispositivo_null"
        )
        token2 = Token(
            token="token_2",
            expiration=datetime.now() + timedelta(days=1000),
            ip="null",
            dispositivo="Dispositivo_null"
        )

        db.session.add_all([token1, token2])
        db.session.commit()

class TokenSchema(ma.Schema):
    class Meta:
        fields = ('token', 'expiration', 'ip', 'dispositivo')
