import json
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

# default route
@views.route("/")
def home():
    return render_template("index.html", value1 = "Corn")

# sample for taking a username as part of url
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", value1 = username)

# sample page to take arguments
@views.route("/getprofile")
def profile2():
    args = request.args
    name = args.get("name")
    return render_template("index.html", value1 = name)

# use content blocks and templates
@views.route("/profile3")
def profile3():
    return render_template("profile.html")

# sample to take json data as parameters
@views.route("/json")
def get_json():
    return jsonify({'name':'corn', 'value2':10})

# sample to return json data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# sample redirect
@views.route("/goto")
def goto():
    return redirect(url_for("views.home"))

