from django.contrib import admin
from cms.models import Data

#admin.site.register(Data)

class DataAdmin(admin.ModelAdmin):
    list_display = ('userdata', 'whatdata', 'datavalue',)
    list_display_links = ('userdata',)
admin.site.register(Data, DataAdmin)
