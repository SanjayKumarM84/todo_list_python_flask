from init import *
from common_modules.modules import uuid_func


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(50), primary_key=True, default=lambda: uuid_func())
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate = func.now())
    deleted_at = db.Column(db.DateTime(timezone=True), default = None)
