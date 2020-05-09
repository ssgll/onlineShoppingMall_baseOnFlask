#! coding:utf-8
from app import indexBlueprint, authBlueprint
from app.views.index import indexView, logoutView, passwordManager
from app.views.register import registerView
from app.views.userManagement import userManager

indexBlueprint.add_url_rule("/", 'index', indexView, methods=["GET", "POST"])
indexBlueprint.add_url_rule("/logout", 'logout', logoutView, methods=["GET", "POST"])
indexBlueprint.add_url_rule("/passwordupdate", "passwordManage", passwordManager, methods=["POST", "GET"])


authBlueprint.add_url_rule("/register", 'register', registerView, methods=["GET", "POST"])
authBlueprint.add_url_rule("/usermanager/", "usermanager", userManager, methods=["GET", "POST"])
