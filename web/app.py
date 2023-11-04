from flask import Flask, render_template
import json as jx

app = Flask(__name__)

def isMasterPassword(pswd):
    save = open("save.json")
    if (jx.loads(save.read)["master_pswd"] == pswd):
        save.close()
        return True
    else :
        save.close()
        return False
    
@app.route("/")
def hello_world():
    return render_template("home.html")