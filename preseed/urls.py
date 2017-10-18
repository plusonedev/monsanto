from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<instance_id>[\w{}.-]{1,40})/$', views.detail, name='instance'),
]

