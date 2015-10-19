from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^get_top_result$', views.getTopResult, name='getTopResult'),
)
