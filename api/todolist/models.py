from common_modules.models import *

class TodoList(BaseModel):
    __tablename__ = "todolist_data"

    description = db.Column(db.Text)
    user_id = db.Column(db.String(50))
    days = db.Column(db.JSON)
    date = db.Column(db.String(20))
