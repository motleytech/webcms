from django.conf.urls import patterns, url
from cmsplugin_pybook import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    url(r'^custom.css$', views.customcss, name='customcss'),
    url(r'^(?P<bookname>.+)$', views.showbook, name='showbook'),
)