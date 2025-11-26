from django.contrib import admin
from .models import Paciente, BeckResultado

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'dni', 'genero', 'telefono', 'fecha_nacimiento']
    list_select_related = ['user']
    search_fields = ['dni', 'user__username', 'user__email']

class BeckResultadoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'puntuacion', 'nivel']
    list_select_related = ['paciente']
    list_filter = ['nivel']
    search_fields = ['paciente__username', 'paciente__email']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(BeckResultado, BeckResultadoAdmin)

# Register your models here.
