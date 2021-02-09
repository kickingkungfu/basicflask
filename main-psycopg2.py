from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlaclchemy.orm import scoped_session, sessionmaker
import psycopg2

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("landing.html") 

@app.route("/cbp")
def cbp():
    return render_template("cbp1.html") 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


