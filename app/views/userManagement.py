# -*- coding: utf-8 -*-
from flask import render_template, session, request, redirect, url_for, flash
from app.models import db, user
from flask_login import login_required


@login_required
def userManager():
    id = session["id"]
    users = db.session.query(user).filter_by(userID=id).one()
    if request.method == "POST":
        username = request.form.get("username")
        tel = request.form.get("tel")
        address = request.form.get("address")
        data = {
            "username": username,
            "tel": tel,
            "address": address
        }
        db.session.query(user).filter_by(userID=id).update(data)
        db.session.commit()
        flash("已保存")
        users = db.session.query(user).filter_by(userID=session["id"]).one()
        return redirect(url_for("authBlueprint.usermanager", users=users))
    return render_template(
        "userManagement.html",
        users=users
    )