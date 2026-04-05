import base64
from config import DevConfig
from model import db, User


def load_to_rdb(last_name, last_4_digits, image_str):
    last_name = last_name
    last_4_digits = last_4_digits

    db.session.add(User(name=last_name, password=last_4_digits))
    db.session.commit()

    return {'message': f'User {last_name} created successfully'}, 201





if __name__ == '__main__':
    db.create_all()
    load_to_rdb()