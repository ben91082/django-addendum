from django.conf.urls import patterns, include, url
from django.contrib import admin

from organizations.backends import invitation_backend, registration_backend

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view=TemplateView.as_view(template_name="home.html"),
        name="home"),
)
