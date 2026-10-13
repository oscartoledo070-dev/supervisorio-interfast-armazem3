# app.py
from flask import Flask, render_template, request
from config import MOTORES_INICIAIS
from automation import calcular_automacao

app = Flask(__name__)

motores_estado = MOTORES_INICIAIS.copy()

@app.route("/", methods=["GET", "POST"])
def index():
    temp = 26.5
    umidade = 62.0
    chuva = False
    
    if request.method == "POST":
        temp = float(request.form.get("temp", 26.5))
        umidade = float(request.form.get("umidade", 62.0))
        chuva = "chuva" in request.form

    global motores_estado
    motores_estado = calcular_automacao(motores_estado, temp, chuva, umidade, request.form)

    return render_template("index.html", 
                           motores=motores_estado, 
                           temp=temp, 
                           umidade=umidade, 
                           chuva=chuva)

if __name__ == "__main__":
    app.run(debug=True, port=5000)