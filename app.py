"""Blogly application."""

from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'


toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def back_to_list():
    """back to user list which is home-page"""
    return redirect("/users")


@app.route('/users')
def list_user():
    """showing list of users"""
    user=User.query.order_by(User.first_name,User.last_name).all()
    return render_template("list.html",user=user)


@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """showing detail of user"""
    user=User.query.get_or_404(user_id)
    return render_template("detail.html",user=user)

@app.route('/users/new', methods=['GET'])
def get_new_user_form():
    ''' showing a form to create a new user'''
    return render_template('new_user.html')

@app.route('/users/new', methods=['POST'])
def new_user():
    ''' adding new user with post method  and redirecting to user list'''

    first_name=request.form['first_name']
    last_name=request.form['last_name']
    image_url=request.form['image_url'] or None 

    new_guy= User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_guy)
    db.session.commit()

    return redirect('/users')



@app.route('/users/<int:user_id>/edit')
def user_edit_page(user_id):
    """show a form to edit an existing user"""

    user=User.query.get_or_404(user_id)
    return render_template('/edit.html',user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_or_edit(user_id):
    """Handling form submission from edit page"""

    user=User.query.get_or_404(user_id)
    user.first_name=request.form['first_name']
    user.last_name=request.form['last_name']
    user.image_url=request.form['image_url'] 

    
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def deleting_user(user_id):
    '''handle form submission from delete button/deleting the user'''
    user=User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")