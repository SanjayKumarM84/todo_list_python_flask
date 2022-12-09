from common_modules.models import *

class UserData(BaseModel):
    __tablename__ = "user_data"

    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40))
    phone_no = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(200))
