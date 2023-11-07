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
        return FileNotFoundError
    
def getBtnClr():
    try:
        sr = open("save.json")
        save = jx.loads(sr.read())
        return save["btnclr"]
    except FileNotFoundError:
        return FileNotFoundError
    
def getBtnLnClr():
    try:
        sr = open("save.json")
        save = jx.loads(sr.read())
        return save["btnlnclr"]
    except FileNotFoundError:
        return FileNotFoundError
    
def getBtnTxtClr():
    try:
        sr = open("save.json")
        save = jx.loads(sr.read())
        return save["btntxtclr"]
    except FileNotFoundError:
        return FileNotFoundError
    
def getSNAME():
    try:
        sr = open("save.json")
        save = jx.loads(sr.read())
        return save["sname"]
    except FileNotFoundError:
        return FileNotFoundError

@app.route("/")
def home():
    return render_template("home.html", wt=getHomePageSave()["welcometext"], name=getHomePageSave()["pagetitle"], bc = getBtnClr(), blc = getBtnLnClr(), btc = getBtnTxtClr(), version = ver, sname = getSNAME())

@app.route("/login")
def login():
    return render_template("login.html", name=getHomePageSave()["pagetitle"])