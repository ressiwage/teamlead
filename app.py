from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy #
import random, os

app=Flask(__name__)
            
@app.route('/', methods=['GET', 'POST'])
def index():            
    return render_template("base.html")

@app.route('/<string:defined_page>')
def custom(defined_page):
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)