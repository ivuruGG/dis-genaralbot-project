from flask import Blueprint, redirect, request, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from dashboard.models import User
from dashboard.utils.auth import hash_password, verify_password

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = bool(request.form.get("remember_me"))

        user = User.query.filter_by(username=username).first()

        if user is None or not verify_password(password, user.password):
            flash("Invalid username or password")
            return redirect(url_for("login.login"))

        login_user(user, remember=remember_me)

        next_page = request.args.get("next")

        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("home.index")

        return redirect(next_page)

    return render_template("login.html")


@login_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.index"))
