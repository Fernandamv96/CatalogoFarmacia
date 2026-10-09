from django.contrib import admin
from .models import CatalogoFarmacia

@admin.register(CatalogoFarmacia)
class CatalogoFarmaciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'fecha_vencimiento', 'esta_vencido')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_vencimiento',)
