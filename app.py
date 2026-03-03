from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# Storage en memoria (lista de notas)
notas = []
contador_id = 1

ETIQUETAS_DISPONIBLES = ["trabajo", "personal", "ideas", "urgente", "estudio"]


def buscar_nota(nota_id):
    return next((n for n in notas if n["id"] == nota_id), None)


def filtrar_notas(busqueda="", etiqueta=""):
    resultado = notas

    if etiqueta:
        resultado = [n for n in resultado if etiqueta in n["etiquetas"]]

    if busqueda:
        busqueda = busqueda.lower()
        resultado = [
            n for n in resultado
            if busqueda in n["titulo"].lower() or busqueda in n["contenido"].lower()
        ]

    return resultado


@app.route("/")
def index():
    busqueda = request.args.get("q", "")
    etiqueta = request.args.get("etiqueta", "")
    notas_filtradas = filtrar_notas(busqueda, etiqueta)

    return render_template(
        "index.html",
        notas=notas_filtradas,
        etiquetas=ETIQUETAS_DISPONIBLES,
        busqueda=busqueda,
        etiqueta_activa=etiqueta,
        total=len(notas)
    )


@app.route("/crear", methods=["POST"])
def crear_nota():
    global contador_id

    titulo = request.form.get("titulo", "").strip()
    contenido = request.form.get("contenido", "").strip()
    etiquetas_sel = request.form.getlist("etiquetas")

    if not titulo or not contenido:
        return redirect(url_for("index"))

    nota = {
        "id": contador_id,
        "titulo": titulo,
        "contenido": contenido,
        "etiquetas": etiquetas_sel,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    notas.append(nota)
    contador_id += 1

    return redirect(url_for("index"))


@app.route("/eliminar/<int:nota_id>", methods=["POST"])
def eliminar_nota(nota_id):
    global notas
    notas = [n for n in notas if n["id"] != nota_id]
    return redirect(url_for("index"))


@app.route("/editar/<int:nota_id>", methods=["GET", "POST"])
def editar_nota(nota_id):
    nota = buscar_nota(nota_id)

    if not nota:
        return redirect(url_for("index"))

    if request.method == "POST":
        nota["titulo"] = request.form.get("titulo", "").strip()
        nota["contenido"] = request.form.get("contenido", "").strip()
        nota["etiquetas"] = request.form.getlist("etiquetas")
        nota["fecha"] = datetime.now().strftime("%d/%m/%Y %H:%M") + " (editado)"
        return redirect(url_for("index"))

    return render_template(
        "editar.html",
        nota=nota,
        etiquetas=ETIQUETAS_DISPONIBLES
    )


if __name__ == "__main__":
    app.run(debug=True)
