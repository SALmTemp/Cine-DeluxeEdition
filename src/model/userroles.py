from config.db import db, app, ma

class UserRoles(db.Model):
    __tablename__ = "tblusersroles"

    rol_id = db.Column(db.Integer, primary_key=True)
    rol_name = db.Column(db.String(50))
    

    def __init__(self,rol_id, rol_name):
        self.rol_id= rol_id
        self.rol_name = rol_name
        

        with app.app_context():
            db.create_all()

class UserRolesSchema(ma.Schema):
    class Meta:
        fields = ('rol_id','rol_name')