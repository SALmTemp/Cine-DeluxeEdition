from config.db import db, app, ma

class Estados(db.Model):
    __tablename__ = "tblestados"

    estado_id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=False)
    is_suspended_account = db.Column(db.Boolean, default=False)
    is_delete_account = db.Column(db.Boolean, default=False)
    last_active = db.Column(db.DateTime, nullable=False)
    notifications = db.Column(db.Text)
    

    def __init__(self,is_active,is_suspended_account,is_delete_account,last_active,notifications):
        self.is_active = is_active
        self.is_suspended_account = is_suspended_account
        self.is_delete_account = is_delete_account
        self.last_active = last_active
        self.notifications = notifications
        

with app.app_context():
    db.create_all()

class EstadosSchema(ma.Schema):
    class Meta:
        fields = ('is_active', 'is_suspended_account', 'is_delete_account', 'last_active', 'notifications')