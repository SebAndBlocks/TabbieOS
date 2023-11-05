from flask import Flask, render_template, abort
import json as jx

app = Flask(__name__)
ver = "0.1"

def getHomePageSave():
    try:
        sraw = open("save.json")
        sjson = jx.loads(sraw.read())
        return sjson["home_page"]
    except FileNotFoundError:
        return FileNotFoundError

def isMasterPassword(pswd):
    try:
        save = open("save.json")
        if (jx.loads(save.read)["master_pswd"] == pswd):
            save.close()
            return True
        else :
            save.close()
            return False
    except FileNotFoundError:
        return "nosave"
    
@app.route("/")
def home():
    return render_template("home.html", wt=getHomePageSave()["welcometext"], name=getHomePageSave()["pagetitle"])
