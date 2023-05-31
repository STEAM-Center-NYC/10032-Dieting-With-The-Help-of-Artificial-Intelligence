from flask import Flask, render_template, request, redirect, send_from_directory, abort, g

from flask_login import LoginManager, login_required, login_user, current_user, logout_user

import pymysql
import pymysql.cursors

import pandas as pd
import numpy as np

login_manager = LoginManager()




app = Flask(__name__)
login_manager.init_app(app)



@login_manager.user_loader
def user_loader(user_id):
     cursor = get_db().cursor()

     cursor.execute("SELECT * from `user` WHERE `id` =" + user_id)




     result = cursor.fetchone()

     if result is None:
          return None
     
     return User(result['ID'],result['username'],result['banned'])

@app.route("/")
def index():

    return render_template(
        "home.html.jinja"
        

    )

@app.route("/about")
def about():

    return render_template(
        "about.html.jinja"
        

    )


@app.route("/Diets")
def diets():

    return render_template(
        "diets.html.jinja"
        

    )

@app.route("/vegan")
def vegan():

    df = pd.read_csv('/Users/ECU/Downloads/archive/vegan.csv',sep=',')
    df.head()

    return render_template(
        "vegan.html.jinja"
        

    )

@app.route("/Paleo")
def paleo():

    return render_template(
        "Paleo.html.jinja"
        

    )

@app.route("/Dash")
def dash():

    return render_template(
        "Dash.html.jinja"
        

    )

@app.route("/mediterranean")
def med():

    return render_template(
        "mediterranean.html.jinja"
        

    )

@app.route("/keto")
def keto():

    return render_template(
        "keto.html.jinja"
        

    )






@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.jinja'),404

if __name__=='__main__':
     app.run(debug=True)


