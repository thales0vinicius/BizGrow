from flask import Flask, render_template, redirect
import mysql.connector

app = Flask(__name__)

# conexaoDB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database=""
# )

@app.route('/')
def home():
    # comandoSQL = 'SELECT * FROM Vagas'
    # cursorDB = conexaoDB.cursor()
    # cursorDB.execute(comandoSQL)
    # vagas = cursorDB.fetchall()
    # cursorDB.close()
    # return render_template("home.html", vagas=vagas)
    return render_template("home.html")

app.run(host='0.0.0.0',port=5000, debug=True)