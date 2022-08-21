from flask_admin import expose, AdminIndexView
from util import count_employes

class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/adminindex.html', msg = count_employes())