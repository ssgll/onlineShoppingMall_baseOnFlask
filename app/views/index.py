#! coding:utf-8
from flask import render_template, request, session, redirect, url_for, make_response
from app.validate import loginValidator
from flask_login import login_required, logout_user, login_user
from app.models import db, user


def indexView():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = loginValidator(username=username, password=password).checkoutReturn()
        # response = make_response("Success")
        # response.set_cookie("name", username, expires=datetime.now()+timedelta(hours=1))
        # cookie = request.cookies.get("name")
        user_info = login_user(username)
        if not error:
            session["username"] = username
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