from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Marco BG'}
    posts = [
        {
            'author': {'username': 'marco1'},
            'body': 'How are you buddy 1'
        },
        {
            'author': {'username': 'marco2'},
            'body': 'Good and you m8 2'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
