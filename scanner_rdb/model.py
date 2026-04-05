from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    last_four_digits = db.Column(db.String(4), unique=False, nullable=False)
    image_str = db.Column(db.String(200), unique=False, nullable=False)
    # image_vector = db.Column(db.PickleType, unique=False, nullable=False)
    

    def __init__(self, last_name, last_four_digits, image_str):
        self.last_name = last_name
        self.last_four_digits = last_four_digits
        self.image_str = image_str

    def __repr__(self):
        return f"{self.last_name} ({self.last_four_digits}) {self.image_str or ''}"
