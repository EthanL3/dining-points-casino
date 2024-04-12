from flask import Flask, render_template, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# # User model for demonstration
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     tokens = db.Column(db.Integer, default=0)

tokens = {'admin':0}

@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('dashboard'))

# Dummy data for surveys
surveys = [
    {"id": 1, "title": "Survey 1", "description": "Description of Survey 1", 'status':'Not started'},
    {"id": 2, "title": "Survey 2", "description": "Description of Survey 2", 'status':'Incomplete'},
    {"id": 3, "title": "Survey 3", "description": "Description of Survey 3", 'status':'Complete'}
]
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', surveys=surveys, tokens=tokens['admin'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/wheel')
def wheel():
    tokens['admin'] -= 1
    return render_template('wheel.html')

survey_information = [
    {"id": 1, "title": "Survey 1", "description": "Description of Survey 1", 'status':'Not started', 'questions':[
        {'question':'What is your name?', 'type':'text'},
        {'question':'What is your age?', 'type':'number'},
        {'question':'Are you an undergraduate student?', 'type':'radio', 'options':['Yes', 'No']}
        ]},
    {"id": 2, "title": "Survey 2", "description": "Description of Survey 2", 'status':'Incomplete', 'questions':[
        {'question':'What is your major?', 'type':'text'},
        {'question':'How many dogs do you have?', 'type':'number'},
        {'question':'Do you like Python?', 'type':'radio', 'options':['Yes', 'No']}
    ]},
    {"id": 3, "title": "Survey 3", "description": "Description of Survey 3", 'status':'Complete', 'questions':[
        {'question':'What is your favorite class?', 'type':'text'},
        {'question':'What is your gpa?', 'type':'number'},
        {'question':'Do you like BU?', 'type':'radio', 'options':['Yes', 'No']}
    ]}
]
@app.route('/survey/<int:survey_id>')
def survey(survey_id):
    # Find the survey with the given id
    for survey in survey_information:
        if survey['id'] == survey_id:
            return render_template('survey.html', survey=survey)

@app.route('/submit_survey/<int:survey_id>', methods=['POST'])
def submit_survey(survey_id):
    # Assuming the user is logged in and their ID is stored in the session
    # user_id = session.get('user_id')
    # user = User.query.get(user_id)
    # user.tokens += 1
    # db.session.commit()
    # return redirect(url_for('index'))
    tokens['admin'] += 1
    surveys[survey_id-1]['status'] = 'Complete'
    return redirect(url_for('dashboard'))


@app.route('/survey_completed')
def survey_completed():
    # Assuming the user is logged in and their ID is stored in the session
    # user_id = session.get('user_id')
    # user = User.query.get(user_id)
    # user.tokens += 1  # Increment tokens
    # db.session.commit()
    # return redirect(url_for('index'))
    return

# add app routes for index 

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])

def login_post():
    # Assuming the user is logged in and their ID is stored in the session
    # user_id = session.get('user_id')
    # user = User.query.get(user_id)
    # user.tokens += 1  # Increment tokens
    # db.session.commit()
    # return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
