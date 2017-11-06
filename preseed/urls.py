from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<instance_id>[\w{}.-]{1,40})/$', views.detail, name='instance'),   
    url(r'^script/(P<instance_id>[\w{}.-]{1,40})/$', views.post_boot_script, name='script_view'),
]
