from flask_admin import BaseView, expose
from flask_login import login_required, current_user
# from ..decorators import admin_required, permission_required

class CustomView(BaseView):
    """View function of Flask-Admin for Custom page."""

    @expose('/')
    @login_required
    # @admin_required
    def index(self):
        return self.render('admin/index.html')
