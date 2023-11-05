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
        return FileExistsError
    
def getBtnClr():
    try:
        save = open("save.json")
        bc = save.read["btnclr"]
        save.close()
        return bc
    except FileNotFoundError:
        return FileExistsError
    
def getBtnLnClr():
    try:
        save = open("save.json")
        bc = save.read["btnlnclr"]
        save.close()
        return bc
    except FileNotFoundError:
        return FileExistsError
    
def getBtnTxtClr():
    try:
        save = open("save.json")
        bc = save.read["btntxtclr"]
        save.close()
        return bc
    except FileNotFoundError:
        return FileExistsError

@app.route("/")
def home():
    return render_template("home.html", wt=getHomePageSave()["welcometext"], name=getHomePageSave()["pagetitle"], bc = getBtnClr(), blc = getBtnLnClr(), btc = getBtnTxtClr())
