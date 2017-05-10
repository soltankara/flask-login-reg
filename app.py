from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash


from models import *
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# @app.before_first_request
# def create_database():
#      db.create_all()

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()

	error = None

	if request.method == 'POST':
		error = 'Invalid username or password! Please, try again!'
		user = Users.query.filter_by(username = form.username.data).first()

		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember = form.remember.data)
				return redirect(url_for('home'))

	return render_template('login.html', form = form, error = error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():

	form = RegistrationForm()

	if request.method == 'POST':
		username = form.username.data
		email = form.email.data
		password = generate_password_hash(form.password.data, method='sha256')
		user = Users(username = username, password = password, email = email)
		db.session.add(user)
		db.session.commit()

		login_user(user)
		return redirect(url_for('home'))


	return render_template('signup.html', form = form)

@app.route('/home')
@login_required
def home():
	return render_template('home.html', user = current_user.username)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))





if __name__ == '__main__':
	app.run(debug=True)
