from flask_app import app, render_template, request, redirect
from flask_app.models.model_dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    return render_template("dojos.html", dojos= Dojo.get_all())

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/show/<int:id>")
def show(id):
    data= {"id":id}
    return render_template("show.html", dojo= Dojo.get_one(data), dojo_ninjas= Dojo.get_dojo_with_ninjas(data))