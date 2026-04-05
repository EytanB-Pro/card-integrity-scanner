import base64
from flask import Flask
from config import DevConfig
from model import db, User

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)


def load_to_rdb(user_last_name, user_last_four_digits, image):
    last_name = user_last_name
    last_four_digits = user_last_four_digits

    # Check if user already exists
    existing_user = User.query.filter_by(last_name=last_name).first()
    if existing_user:
        return {'message': f'User {last_name} already exists'}, 409

    with open(image, "rb") as image_file:
        image_str = base64.b64encode(image_file.read()).decode('utf-8')

    db.session.add(User(last_name=last_name, last_four_digits=last_four_digits, image_str=image_str))
    db.session.commit()

    return {'message': f'User {last_name} created    successfully'}, 201

def return_str_to_img(image_str, output_filename="recovered_image.jpg"):
    image_data = base64.b64decode(image_str)
    with open(output_filename, "wb") as f:
        f.write(image_data)
    return f"Image recovered and saved as '{output_filename}'"


def get_user_image(last_name, output_filename=None):
    user = User.query.filter_by(last_name=last_name).first()
    if not user:
        return f"User {last_name} not found"
    
    if output_filename is None:
        output_filename = f"{last_name}_recovered.jpg"
    
    return return_str_to_img(user.image_str, output_filename)


if __name__ == "__main__":
    with app.app_context():
        # Create table if it doesn't exist
        db.create_all()
        
        # Load multiple users with different names
        users_to_load = [
            ("Yakov", "9889"),
            ("Sarah", "1234"),
            ("David", "5678"),
        ]
        
        for last_name, last_four in users_to_load:
            result = load_to_rdb(last_name, last_four, "test_images/IMG_5007.jpg")
            print(f"{last_name}: {result}")
        
        # Retrieve and save images
        for last_name, _ in users_to_load:
            result = get_user_image(last_name)
            print(result)