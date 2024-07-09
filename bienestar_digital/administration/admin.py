from django.contrib.admin import AdminSite
from django.urls.resolvers import URLResolver
from django.http import HttpResponse
from home.forms import LoginForm
from django.urls import path

# Register your models here.

class Administration(AdminSite):

    def get_urls(self) -> list[URLResolver]:
        urls = super().get_urls()
        urls[14]=path('asistences/download_excel', self.admin_view(self.download_excel), name='download_asistences')
        return urls

    def download_excel(self, req):
        from .services import create_asistences_excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        create_asistences_excel(response)
        return response

    def __init__(self, name: str = 'admin') -> None:
        super().__init__(name)
        self.site_header = 'Bienestar Digital Administration'
        self.site_title = 'Bienestar Digital'
        self.index_title = 'Admin'
        self.login_template = 'login.html'
        self.logout_template = 'administration_logout.html'
        self.index_template = 'administration_index.html'
        self.login_form = LoginForm
    pass
pass
administration_site=Administration()