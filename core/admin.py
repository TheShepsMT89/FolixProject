from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Topic)
admin.site.register(Subtopic)

admin.site.site_header = "La Administración Folix"
admin.site.site_title = "Administración de Folix"
admin.site.index_title = "Panel administrador"
