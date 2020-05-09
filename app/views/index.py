#! coding:utf-8
from flask import render_template, request, session, redirect, url_for, flash
from app.validate import loginValidator
from flask_login import login_required, logout_user, login_user
from app.models import db, user
from werkzeug.security import check_password_hash, generate_password_hash


def indexView():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = loginValidator(username=username, password=password).checkoutReturn()
        # response = make_response("Success")
        # response.set_cookie("name", username, expires=datetime.now()+timedelta(hours=1))
        # cookie = request.cookies.get("name")
        if not error:
            session["username"] = username
            users = db.session.query(user).filter_by(username=username).first()
            login_user(users)
            session["id"] = db.session.query(user).filter_by(username=username).one().userID
            return render_template(
                "index.html",
                username=session.get("username")
            )
        return render_template(
            "index.html",
            error=error
        )
    return render_template(
        "index.html",
        username=session.get("username")
    )


@login_required
def logoutView():
    session.clear()
    logout_user()
    return redirect(url_for("indexBlueprint.index"))


@login_required
def passwordManager():
    if request.method == "POST":
        oldPasswordHash = db.session.query(user).filter_by(userID=session["id"]).first().password_hash
        newPassword = request.form.get("newPassword")
        oldPassword = request.form.get("oldPassword")
        if check_password_hash(oldPasswordHash, oldPassword):
            newPasswordHash = generate_password_hash(newPassword)
            db.session.query(user).filter_by(userID=session["id"]).update({"password_hash": newPasswordHash})
            db.session.commit()
            flash("修改成功")
        else:
            flash("修改失败")
    return render_template("passwordMnager.html")
