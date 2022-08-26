from django.contrib import admin
from .models import metas, metas_dia, avaliacao, disponibilidade, nc_financeiro, lista, promocoes, tempo, lojas


# Register your models here.

admin.site.register(lista)
admin.site.register(nc_financeiro)
admin.site.register(disponibilidade)
admin.site.register(avaliacao)
admin.site.register(tempo)
admin.site.register(promocoes)
admin.site.register(lojas)
admin.site.register(metas)
admin.site.register(metas_dia)