from config.db import db, app, ma

class Token(db.Model):
    __tablename__ = "tbltoken"

    id_token = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200))
    expiration = db.Column(db.DateTime)
    ip = db.Column(db.String(200)) 
    dispositivo = db.Column(db.String(200)) 

    def __init__(self, token,expiration,ip,dispositivo):
        self.token = token
        self.expiration = expiration
        self.ip = ip
        self.dispositivo = dispositivo
        

with app.app_context():
    db.create_all()

class TokenSchema(ma.Schema):
    class Meta:
        fields = ('token', 'expiration', 'ip', 'dispositivo')