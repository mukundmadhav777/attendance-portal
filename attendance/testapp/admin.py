from django.contrib import admin
from testapp.models import Portal
class PortalAdmin(admin.ModelAdmin):
    list_display=['name','desigination','status']
admin.site.register(Portal,PortalAdmin)
