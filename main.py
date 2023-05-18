from flask import Flask, render_template, request,redirect, send_from_directory,abort, g
import pymysql
import pymysql.cursors
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from transformers import AutoTokenizer, AutoModelForCausalLM




login_manager = LoginManager()



app = Flask(__name__)
login_manager.init_app(app)


app.config['SECRET_KEY'] = 'something_random'






#Home page
@app.route("/")
def index():

    return render_template(
        "home.html.jinja"
        
    )


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.jinja'),404     

if __name__=='__main__':
     app.run(debug=True)
