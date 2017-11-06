from django.contrib import admin
from .models import PreseedInstance

class PreseedInstanceAdmin(admin.ModelAdmin):
    list_display = ('instance_id', 'preseed_url_field', 'script_url_field', 'updated_at')
    
    def preseed_url_field(self, obj):
        return '<a href="%s%s%s" target="_blank">%s</a>' % ('/preseeds/', obj.instance_id, '/', 'view preseed')
    
    preseed_url_field.allow_tags = True
    preseed_url_field.short_description = 'Preseed Link'
    
    def script_url_field(self, obj):
        return '<a href="%s%s%s" target="_blank">%s</a>' % ('/scripts/', obj.instance_id, '/', 'view script')
    
    script_url_field.allow_tags = True
    script_url_field.short_description = 'Post-Install Script'

admin.site.register(PreseedInstance, PreseedInstanceAdmin)
admin.site.site_title = "Monsanto administration"
admin.site.site_header = "Monsanto administration"


