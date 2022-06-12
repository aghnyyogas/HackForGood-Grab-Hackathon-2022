from flask import Flask, render_template, url_for, send_file, request, redirect
from flask_mysqldb import MySQL
# from database import db_session, init_db
# from models import LogTbIntegrasi, LogTbModul, MsJenisAkses, MsJenisAplikasi, \
#     MsKategoriCommon, MsKategoriProbis, MsStatusAplikasi, RefKode, TbAppdeploy, \
#     TbIntegrasi, TbModul, MsAplikasi, LogMsAplikasi, TbProfileUnit


app = Flask(__name__)

# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_PORT'] = 3307
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'A3+'

mysql = MySQL(app)

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()


@app.route("/")
def sign_in_page():
    return render_template('index.html')


@app.route("/logout")
def logout():
    return render_template('index.html')

# @app.route("/")
# def sign_in_page():
#     return render_template('sign_in.html')


@app.route("/home", methods=["GET", "POST"])
def sign_in_proses():
    if request.method == "POST":
        user_name = request.form.get("username")
        if user_name == 'resto':
            return render_template("resto.html")
        elif user_name == 'farmer':
            return render_template("farmer.html")
        elif user_name == 'user':
            return render_template("user_food.html")
        else:
            return render_template("404.html")


@app.route("/user_profile")
def user_profile():
    return render_template('input_user_profile.html')


@app.route("/farmer")
def farmer():
    return render_template('farmer.html')


@app.route("/resto")
def resto():
    return render_template('resto.html')


@app.route("/user_food")
def food():
    return render_template('user_food.html')


if __name__ == "__main__":
    app.run(debug=True)
