from django.contrib import admin
from .models import PreseedInstance

admin.site.register(PreseedInstance)
admin.site.site_title = "Monsanto administration"
admin.site.site_header = "Monsanto administration"
