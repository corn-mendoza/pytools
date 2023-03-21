import json
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", value1 = "Corn")

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", value1 = username)

@views.route("/profile2")
def profile2():
    args = request.args
    name = args.get("name")
    return render_template("index.html", value1 = name)

# use content blocks and templates
@views.route("/profile3")
def profile3():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name':'corn', 'value2':10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# redirect
@views.route("/goto")
def goto():
    return redirect(url_for("views.home"))

