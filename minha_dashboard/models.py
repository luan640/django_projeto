from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class nc_financeiro(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restaurante = models.CharField(db_column='restaurante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='data', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='mes', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ano', blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='dia', blank=True, null=True)  # Field name made lowercase.
    total_do_pedido = models.FloatField(db_column='total_do_pedido', blank=True, null=True)  # Field name made lowercase.
    valor_dos_itens = models.FloatField(db_column='valor_dos_itens', blank=True, null=True)  # Field name made lowercase.
    incentivo_ifood = models.FloatField(db_column='incentivo_ifood', max_length=255, blank=True, null=True)  # Field name made lowercase.
    incentivo_loja = models.FloatField(db_column='incentivo_loja', blank=True, null=True)  # Field name made lowercase.
    faturamento_liquido = models.IntegerField(db_column='faturamento_liquido', blank=True, null=True)  # Field name made lowercase.
    valor_de_taxa_de_transacao = models.FloatField(db_column='valor_de_taxa_de_transacao', blank=True, null=True)  # Field name made lowercase.
    valor_de_taxa_de_1_semana = models.FloatField(db_column='valor_de_taxa_de_1_semana', blank=True, null=True)  # Field name made lowercase.
    numero_de_pedidos = models.IntegerField(db_column='numero_de_pedidos', blank=True, null=True)  # Field name made lowercase.
    numero_de_cancelamentos = models.IntegerField(db_column='numero_de_cancelamentos', blank=True, null=True)  # Field name made lowercase.
    valor_bruto_cancelado_na_plataforma = models.IntegerField(db_column='valor_bruto_cancelado_na_plataforma', blank=True, null=True)  # Field name made lowercase.
    valor_liquido_cancelado_na_plataforma = models.IntegerField(db_column='valor_liquido_cancelado_na_plataforma', blank=True, null=True)  # Field name made lowercase.
    taxa_de_entrega = models.FloatField(db_column='taxa_de_entrega', blank=True, null=True)  # Field name made lowercase.
    faturamento_bruto = models.FloatField(db_column='faturamento_bruto', blank=True, null=True)  # Field name made lowercase.
    cancelamento_percent = models.FloatField(db_column='cancelamento_percent', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_cliente = models.FloatField(db_column='cancelamento_pelo_cliente', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_cliente_percent = models.FloatField(db_column='cancelamento_pelo_cliente_percent', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_restaurante = models.FloatField(db_column='cancelamento_pelo_restaurante', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_restaurante_percent = models.FloatField(db_column='cancelamento_pelo_restaurante_percent', blank=True, null=True)  # Field name made lowercase.
    faturamento_real = models.FloatField(db_column='faturamento_real', blank=True, null=True)  # Field name made lowercase.
    ticket_medio = models.FloatField(db_column='ticket_medio', blank=True, null=True)  # Field name made lowercase.
    ticket_medio_real = models.FloatField(db_column='ticket_medio_real', blank=True, null=True)  # Field name made lowercase.
    incentivo_percent = models.FloatField(db_column='incentivo_percent', blank=True, null=True)  # Field name made lowercase.
    taxa_efetiva = models.FloatField(db_column='taxa_efetiva', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='margem', blank=True, null=True)  # Field name made lowercase.
    taxa_de_cancelamento = models.FloatField(db_column='taxa_de_cancelamento', blank=True, null=True)  # Field name made lowercase.
    nps_medio = models.FloatField(db_column='nps_medio', blank=True, null=True)  # Field name made lowercase.
    numero_de_comentarios = models.IntegerField(db_column='numero_de_comentarios', blank=True, null=True)  # Field name made lowercase.
    numero_de_avaliacoes = models.IntegerField(db_column='numero_de_avaliacoes', blank=True, null=True)  # Field name made lowercase.
    valor_da_comissao = models.FloatField(db_column='valor_da_comissao', blank=True, null=True)  # Field name made lowercase.
    repasse_do_ifood = models.FloatField(db_column='repasse_do_ifood', blank=True, null=True)  # Field name made lowercase.
    valor_balcao = models.FloatField(db_column='valor_balcao', blank=True, null=True)  # Field name made lowercase.
    valor_balcao_real = models.FloatField(db_column='valor_balcao_real', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nc_financeiro'
    def __str__(self):
        return self.cliente

class lista(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='lista', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lista'
    def __str__(self):
        return self.cliente

class disponibilidade(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='categoria', max_length=255, blank=True, null=True)  # Field name made lowercase.
    produto = models.CharField(db_column='produto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disponibilidade = models.CharField(db_column='disponibilidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disponibilidade'
    def __str__(self):
        return self.cliente

class promocoes(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    promoção = models.CharField(db_column='promoção', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promocoes'
    def __str__(self):
        return self.cliente

class tempo(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='hora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tempo_de_entrega  = models.CharField(db_column='tempo_de_entrega', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempo'
    def __str__(self):
        return self.cliente

class avaliacao(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Pepedidodido = models.CharField(db_column='pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_do_pedido = models.CharField(db_column='data_do_pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avaliação = models.CharField(db_column='avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_da_avaliação = models.CharField(db_column='data_da_avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comentário = models.CharField(db_column='comentário', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unnamed_6 = models.CharField(db_column='unnamed_6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja  = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avaliacao'
    def __str__(self):
        return self.cliente

class lojas(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lojas  = models.CharField(db_column='lojas', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lojas'
    def __str__(self):
        return self.cliente