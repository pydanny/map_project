from apps.mapper.models import ApplicationType, Application, Mapp
from django.contrib import admin

class ApplicationTypeAdmin(admin.ModelAdmin):
    list_display        = ('title', 'color', 'shape', )
    list_filter         = ('title', )
    search_fields       = ('title',)

admin.site.register(ApplicationType, ApplicationTypeAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display        = ('title', 'application_type', )
    list_filter         = ('title', 'application_type', )
    search_fields       = ('title', 'application_type', )

admin.site.register(Application, ApplicationAdmin)