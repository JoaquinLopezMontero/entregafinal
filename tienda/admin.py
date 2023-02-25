from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_field=("created", "updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto)