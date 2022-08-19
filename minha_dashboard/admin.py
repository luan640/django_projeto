from django.contrib import admin
from .models import avaliacao, disponibilidade, nc_financeiro, lista, promocao, tempo, lojas


# Register your models here.

admin.site.register(lista)
admin.site.register(nc_financeiro)
admin.site.register(disponibilidade)
admin.site.register(avaliacao)
admin.site.register(tempo)
admin.site.register(promocao)
admin.site.register(lojas)