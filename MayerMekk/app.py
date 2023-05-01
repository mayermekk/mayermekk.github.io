from flask import Flask, render_template,redirect, url_for, request
import json


app = Flask(__name__)

fil_service = open("service.json", encoding="utf-8")
service = json.load(fil_service)

fil_chat = open("chat.json", encoding="utf-8")
chat = json.load(fil_chat)
fil_chat.close()

def skriv_chat():
    fil_chat = open("chat.json", "w", encoding="utf-8")
    json.dump(chat, fil_chat)
    fil_chat.close()


@app.route("/")
def rute_index():
    return render_template("index.html")

@app.route("/lokasjon")
def rute_lokasjon():
    return render_template("lokasjon.html")


@app.route("/service")
def rute_service():
    return render_template("service.html", service = service)

@app.route("/servicer/<id>")
def rute_servicer(id):
    return render_template("servicer.html", service = service[id], id=id)


@app.route("/redirect-to-specific-place")
def redirect_to_specific_place():
    return redirect(url_for("rute_service", _anchor="NB-info-boks"))


#@app.route("/chat", methods=["POST", "GET"])
#def rute_chat():
    if request.method == "POST":
        navn = request.form["navn"]
        melding = request.form["melding"]
        chat.insert(0, {
            "navn": navn,
            "melding": melding,
        })
        skriv_chat()
    return render_template("chat.html", chat=chat)



app.run(debug=True, port=5001)
