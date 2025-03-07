from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)