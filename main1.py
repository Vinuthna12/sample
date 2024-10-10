from flask import Flask, make_response, redirect, render_template, request, url_for

app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'Hello {name}'


@app.route('/hello/<name>')
def hello_name(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))
    
@app.route('/admin')
def admin():
    return 'Hello Admin! You\'re welcome to the admin page.'

@app.route('/guest/<guest>')
def guest(guest):
    return f'Hello {guest}'
    
@app.route('/<name>/<int:empid>')
def index(name,empid):
    return render_template('welcome.html',name=name,empid=empid)    
    
if __name__ == '__main__':
    app.run(debug=True)