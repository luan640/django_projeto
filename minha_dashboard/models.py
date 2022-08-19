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

    class Meta:
        managed = False
        db_table = 'nc_financeiro'
    def __str__(self):
        return self.data

class lista(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Lista = models.CharField(db_column='Lista', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja = models.CharField(db_column='Loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Data = models.CharField(db_column='Data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Hora = models.CharField(db_column='Hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lista'
    def __str__(self):
        return self.cliente

class disponibilidade(models.Model):
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Categoria = models.CharField(db_column='Categoria', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Produto = models.CharField(db_column='Produto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Disponibilidade = models.CharField(db_column='Disponibilidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    DATA = models.DateField(db_column='DATA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    LOJA = models.CharField(db_column='LOJA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Hora = models.CharField(db_column='Hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disponibilidade'
    def __str__(self):
        return self.Cliente

class promocao(models.Model):
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Promoção = models.CharField(db_column='Promoção', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    DATA = models.DateField(db_column='DATA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja = models.CharField(db_column='Loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Hora = models.CharField(db_column='Hora', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promocao'
    def __str__(self):
        return self.Cliente

class tempo(models.Model):
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Data = models.CharField(db_column='Data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja = models.CharField(db_column='Loja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Hora = models.CharField(db_column='Hora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Tempo_de_Entrega  = models.CharField(db_column='Tempo_de_Entrega', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempo'
    def __str__(self):
        return self.Cliente

class avaliacao(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Pepedidodido = models.CharField(db_column='pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_do_pedido = models.CharField(db_column='data_do_pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avaliação = models.CharField(db_column='avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_da_avaliação = models.CharField(db_column='data_da_avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comentário = models.CharField(db_column='comentário', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Unnunnamed_6amed_6 = models.CharField(db_column='unnamed_6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loja  = models.CharField(db_column='loja', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avaliacao'
    def __str__(self):
        return self.cliente

class lojas(models.Model):
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja  = models.CharField(db_column='Lojas', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lojas'
    def __str__(self):
        return self.Cliente