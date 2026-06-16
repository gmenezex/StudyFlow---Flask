from app.extensions import db
from datetime import datetime, timezone

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50) )
  email = db.Column(db.String(), unique=True)
  password = db.Column(db.String())
  created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

