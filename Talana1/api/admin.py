from django.contrib import admin
from models import ClUserData


class ClUserDataAdmin(admin.ModelAdmin):
    fields = ['rut', 'Nombre', 'Apellido_1', 'Apellido_2', 'mail' ]


admin.site.register(ClUserData, ClUserDataAdmin)
# Register your models here.
