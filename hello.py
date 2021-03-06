"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
app = Flask(__name__)
name = ''
age = ''
@app.route('/login', methods=['GET', 'POST'])
def login():
    global name, age
    name = request.form['name']
    age = request.form['age']
    fav = request.form['fav']

    print(name)
    print(fav)
    if fav == 'Emily':
        return render_template('profile.html', name = name, age = age)
    else:
        return render_template('error_page.html', name = name, age = age)

@app.route('/redo', methods=['GET', 'POST'])
def redo():
    global name, age
    fav = request.form['fav']

    print(name)
    print(fav)
    if fav == 'Emily':
        return render_template('profile.html', name = name, age = age)
    else:
        return render_template('error_page.html', name = name, age = age)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
