from flask_app import app, render_template, request, redirect
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo



@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route("/ninja/new")
def new():
    return render_template("new.html", dojos= Dojo.get_all())