# coding=utf8
from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config
from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL  # 导入
# from flask_markdown import Markdown
import os
import os.path as op

from flask_admin.contrib import fileadmin
from admin.views import CustomView

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

# flask_admin = Admin()

photos = UploadSet('photos', ALL)  # 创建set

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    configure_uploads(app, photos)  # 初始化

    # path = op.join(op.dirname(__file__), 'static')  # 果然还是应该避免手撸文件路径分割符的
    # print "文件管理", path
    # try:
    #     os.mkdir(path)
        # print "创建文件管理", path
    # except OSError:
    #     pass
    # flask_admin.init_app(app)
    # flask_admin.add_view(CustomView(name='Custom'))
    # flask_admin.add_view(fileadmin.FileAdmin(path, '/static/', name='Files'))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
