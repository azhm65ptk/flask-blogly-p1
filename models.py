from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

DEFAULT_IMAGE_URL="https://picsum.photos/536/354"

def connect_db(app):
    "Connecting the database "
    db.app=app
    db.init_app(app)




class User(db.Model):
    """create a User model for SQLAlchemy."""
    __tablenmae__="user"

    id= db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name= db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    last_name= db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    image_url=db.Column(db.Text,
                    nullable=False,
                    default= DEFAULT_IMAGE_URL)
