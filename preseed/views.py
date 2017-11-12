from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import PreseedInstance

def detail(request, instance_id):
    instance = get_object_or_404(PreseedInstance, instance_id=instance_id.upper())
    
    #parse apps field into an array
    instance.apps = [x.strip() for x in instance.apps.split(',')]
    
    return render(request, 'stretch/template.txt', {'instance': instance}, content_type="text/plain")
   

def post_boot_script(request, instance_id):
    instance = get_object_or_404(PreseedInstance, instance_id=instance_id.upper())
    return render(request, 'stretch/script.sh', {'instance': instance}, content_type="text/plain")

