from flask import Flask, render_template
import json as jx

app = Flask(__name__)

def getHomePageSave():
    sraw = open("save.json")
    sjson = jx.loads(sraw.read())
    return sjson["home_page"]

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
    print(getHomePageSave())
    print(getHomePageSave()["welcometext"])
    print(getHomePageSave()["pagetitle"])
    return render_template("home.html", wt=getHomePageSave()["welcometext"], name=getHomePageSave()["pagetitle"])