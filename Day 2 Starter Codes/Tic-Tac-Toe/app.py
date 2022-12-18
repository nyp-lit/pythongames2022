from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    return redirect(url_for("index"))
    
# def winnerFound(board):
    #check rows
        
    #check cols
        
    #check diagonals
        
    #check if game is drawn

    #game is drawn since there is no winner 
    #and all boxes are filled

if __name__ == "__main__":
    app.run(debug=True)