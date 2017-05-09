from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import datetime

db = SQLAlchemy()

class Users(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column('id', db.Integer, primary_key=True)
	username = db.Column('username', db.String(80), unique = True)
	email = db.Column('email', db.String(80), unique = True)
	password = db.Column('password', db.String(255))
	name = db.Column('name', db.String(255))
	surname = db.Column('surname', db.String(255))
	regDate = db.Column('reg_date', db.DateTime, default=datetime.datetime.utcnow)
	phone = db.Column('phone', db.String(255))
	state = db.Column('state', db.Integer)

class Brands(db.Model):
	__tablename__ = 'brands'
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(255), unique = True)
	state = db.Column('state', db.Integer)


class Models(db.Model):
	__tablename__ = 'models'
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(255), unique = True)
	fkBrandID = db.Column('fk_brand_id', db.Integer, db.ForeignKey('brands.id'))
	state = db.Column('state', db.Integer)


class Products(db.Model):
	__tablename__ = 'products'
	id = db.Column('id', db.Integer, primary_key = True)
	fkModelID = db.Column('fk_model_id', db.Integer, db.ForeignKey('models.id'))
	year = db.Column('year', db.String(4))
	km = db.Column('km', db.String(255))
	fee = db.Column('fee', db.String(255))
	fkUserUsername = db.Column('fk_user_username', db.String(255), db.ForeignKey('users.username'))
	regDate = db.Column('reg_date', db.DateTime, default=datetime.datetime.utcnow)
	otherDetails = db.Column('other_details', db.String(4000))
	state = db.Column('state', db.Integer)


class Roles(db.Model):
	__tablename__ = 'roles'
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(255), unique = True)
	state = db.Column('state', db.Integer)

class Operations(db.Model):
	__tablename__ = 'operations'
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(255), unique = True)
	state = db.Column('state', db.Integer)

class Menus(db.Model):
	__tablename__ = 'menus'
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(255), unique = True)
	state = db.Column('state', db.Integer)


class Role2Username(db.Model):
	__tablename__ = 'role_2_username'
	id = db.Column('id', db.Integer, primary_key=True)
	fkRoleID = db.Column('fk_role_id', db.Integer, db.ForeignKey('roles.id'))
	fkUserUsername = db.Column('fk_user_username', db.String(255), db.ForeignKey('users.username'))
	state = db.Column('state', db.Integer)

class Menu2Role(db.Model):
	__tablename__ = 'menu_2_role'
	id = db.Column('id', db.Integer, primary_key=True)
	fkRoleID = db.Column('fk_role_id', db.Integer, db.ForeignKey('roles.id'))
	fkMenuID = db.Column('fk_menu_id', db.Integer, db.ForeignKey('menus.id'))
	state = db.Column('state', db.Integer)

class Oper2Role(db.Model):
	__tablename__ = 'oper_2_role'
	id = db.Column('id', db.Integer, primary_key=True)
	fkRoleID = db.Column('fk_role_id', db.Integer, db.ForeignKey('roles.id'))
	fkOperID = db.Column('fk_oper_id', db.Integer, db.ForeignKey('operations.id'))
	state = db.Column('state', db.Integer)

class Orders(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	fkUserUsername = db.Column('fk_user_username', db.String(255), db.ForeignKey('users.username'))
	fkProductID = db.Column('fk_product_id', db.Integer, db.ForeignKey('products.id'))
	regDate = db.Column('reg_date', db.DateTime, default=datetime.datetime.utcnow)
	state = db.Column('state', db.Integer)

class Media(db.Model):
	__tablename__ = 'media'
	id = db.Column('id', db.Integer, primary_key=True)
	fkProductID = db.Column('fk_product_id', db.Integer, db.ForeignKey('products.id'))
	path = db.Column('path', db.String(255), unique = True)
	state = db.Column('state', db.Integer)
