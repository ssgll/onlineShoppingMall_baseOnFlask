#! coding:utf-8
from flask import Flask
from config import config
from app.urls import indexBlueprint, authBlueprint
from app.models import db, user
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from importlib import reload
from flask_session import Session
from flask_login import LoginManager
import sys

reload(sys)


# 生成app
def create_app():
    app = Flask(
        __name__,
        template_folder=config["Default"].TEMPLATE_FOLDER,
        static_folder=config["Default"].STATIC_FOLDER
    )
    app.config.from_object(config["Default"])  # 加载配置文件
    return app


# 实例化app
app = create_app()

# 数据库配置
db.init_app(app=app)
migrate = Migrate(app=app, db=db)

# 注册蓝图
app.register_blueprint(indexBlueprint)
app.register_blueprint(authBlueprint)

# session
Session(app)

# 登录设置
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "indexBlueprint.indedx"


@loginManager.user_loader  # 定义获取登录用户的方法
def load_user(user_id):
    return user.get_id(user_id)


# 初始化命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
