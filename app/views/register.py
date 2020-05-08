# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, session, url_for
from app.validate import registerValidate
from app.models import db, user


def registerView():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = registerValidate(username, password, password2).results()
        if not error:
            insertUser = user(username, password)
            db.session.add(insertUser)
            db.session.commit()
            session["username"] = username
            return redirect(url_for("indexBlueprint.index"))
        return render_template(
            "register.html",
            error=error
        )
    return render_template(
        "register.html"
    )