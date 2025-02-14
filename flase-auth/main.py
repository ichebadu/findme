from flask import Flask, render_template,request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "ichekey"

#Configure SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


#Database Model
class User(db.Model):
    #class variables
    id
    username
    password


#Routes
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")


if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)