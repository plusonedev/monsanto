from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from preseed.models import PreseedInstance

def detail(request, instance_id):
    instance = get_object_or_404(PreseedInstance, instance_id=instance_id.upper())

    instance.apps = [x.strip() for x in instance.apps.split(',')]
    
    return render(request, 'post_install', {'instance': instance}, content_type="text/plain")
