from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def to_home_page():  # put application's code here
    return redirect('/home')

@app.route('/home')
def print_welcome():
    return 'Welcome!'


@app.route('/about')
def use_home_def():
    return redirect(url_for('print_welcome'))

if __name__ == '__main__':
    app.run(debug=True)



