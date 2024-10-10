from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/<name>/<int:age>')
def welcome(name, age):
    return render_template('welcome.html', name=name, age = age)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    sites = ['amazon', 'twitter', 'facebook', 'google', 'apple']
    return render_template('about.html', sites=sites)

if __name__=="__main__":
    app.run(debug=True)