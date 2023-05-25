from flask import Flask, render_template, request, redirect, send_from_directory, abort, g

from flask_login import LoginManager, login_required, login_user, current_user, logout_user, get_db, User

import pymysql
import pymysql.cursors

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
def about():

    return render_template(
        "diets.html.jinja"
        

    )





@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.jinja'),404

if __name__=='__main__':
     app.run(debug=True)


