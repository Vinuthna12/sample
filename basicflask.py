from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "home page"

@app.route('/',methods=["GET","POST"])
