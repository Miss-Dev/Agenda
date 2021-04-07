from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'telefone')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
