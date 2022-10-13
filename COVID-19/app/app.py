from flask import Flask, jsonify, request, render_template
from Models import db, confirmed, recovered, deaths
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\confirmados_database.db"
app.config['SQLALCHEMY_BINDS'] = {
    'recovered': "sqlite:///database\\recuperados_database.db",
    'deaths': "sqlite:///database\\decesos_database.db" 
}
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\recuperados_database.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\confirmados_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#Aqui empiezan las rutas
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/api/confirmed")
def getConfirmed():
    try:
        confirmados = confirmed.query.all()
        toReturn = [confirmado.serialize() for confirmado in confirmados]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg":"Ha ocurrido un error"}), 500
        

@app.route("/api/recovered")
def getRecovered():
    try:
        recuperados = recovered.query.all()
        toReturn = [recuperado.serialize() for recuperado in recuperados]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg":"Ha ocurrido un error"}), 500


@app.route("/api/deaths")
def getDeaths():
    try:
        decesos = deaths.query.all()
        toReturn = [deceso.serialize() for deceso in decesos]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg":"Ha ocurrido un error"}), 500




if __name__ == "__main__":
    app.run(debug=True, port = 4000)
