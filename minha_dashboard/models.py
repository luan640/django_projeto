from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class nc_financeiro(models.Model):
    cliente = models.CharField(db_column='cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restaurante = models.CharField(db_column='RESTAURANTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='MES', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='DIA', blank=True, null=True)  # Field name made lowercase.
    total_do_pedido = models.FloatField(db_column='TOTAL_DO_PEDIDO', blank=True, null=True)  # Field name made lowercase.
    valor_dos_itens = models.FloatField(db_column='VALOR_DOS_ITENS', blank=True, null=True)  # Field name made lowercase.
    incentivo_ifood = models.CharField(db_column='INCENTIVO_IFOOD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    incentivo_loja = models.FloatField(db_column='INCENTIVO_LOJA', blank=True, null=True)  # Field name made lowercase.
    faturamento_liquido = models.IntegerField(db_column='FATURAMENTO_LIQUIDO', blank=True, null=True)  # Field name made lowercase.
    valor_de_taxa_de_transacao = models.FloatField(db_column='VALOR_DE_TAXA_DE_TRANSACAO', blank=True, null=True)  # Field name made lowercase.
    valor_de_taxa_de_1_semana = models.FloatField(db_column='VALOR_DE_TAXA_DE_1_SEMANA', blank=True, null=True)  # Field name made lowercase.
    numero_de_pedidos = models.IntegerField(db_column='NUMERO_DE_PEDIDOS', blank=True, null=True)  # Field name made lowercase.
    numero_de_cancelamentos = models.IntegerField(db_column='NUMERO_DE_CANCELAMENTOS', blank=True, null=True)  # Field name made lowercase.
    valor_bruto_cancelado_na_plataforma = models.IntegerField(db_column='VALOR_BRUTO_CANCELADO_NA_PLATAFORMA', blank=True, null=True)  # Field name made lowercase.
    valor_liquido_cancelado_na_plataforma = models.IntegerField(db_column='VALOR_LIQUIDO_CANCELADO_NA_PLATAFORMA', blank=True, null=True)  # Field name made lowercase.
    taxa_de_entrega = models.FloatField(db_column='TAXA_DE_ENTREGA', blank=True, null=True)  # Field name made lowercase.
    faturamento_bruto = models.FloatField(db_column='FATURAMENTO_BRUTO', blank=True, null=True)  # Field name made lowercase.
    cancelamento_percent = models.FloatField(db_column='CANCELAMENTO_PERCENT', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_cliente = models.IntegerField(db_column='CANCELAMENTO_PELO_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_cliente_percent = models.FloatField(db_column='CANCELAMENTO_PELO_CLIENTE_PERCENT', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_restaurante = models.IntegerField(db_column='CANCELAMENTO_PELO_RESTAURANTE', blank=True, null=True)  # Field name made lowercase.
    cancelamento_pelo_restaurante_percent = models.FloatField(db_column='CANCELAMENTO_PELO_RESTAURANTE_PERCENT', blank=True, null=True)  # Field name made lowercase.
    faturamento_real = models.FloatField(db_column='FATURAMENTO_REAL', blank=True, null=True)  # Field name made lowercase.
    ticket_medio = models.FloatField(db_column='TICKET_MEDIO', blank=True, null=True)  # Field name made lowercase.
    ticket_medio_real = models.FloatField(db_column='TICKET_MEDIO_REAL', blank=True, null=True)  # Field name made lowercase.
    incentivo_percent = models.FloatField(db_column='INCENTIVO_PERCENT', blank=True, null=True)  # Field name made lowercase.
    taxa_efetiva = models.FloatField(db_column='TAXA_EFETIVA', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='MARGEM', blank=True, null=True)  # Field name made lowercase.
    taxa_de_cancelamento = models.FloatField(db_column='TAXA_DE_CANCELAMENTO', blank=True, null=True)  # Field name made lowercase.
    nps_médio = models.FloatField(db_column='NPS_MÉDIO', blank=True, null=True)  # Field name made lowercase.
    numero_de_comentários = models.IntegerField(db_column='NÚMERO_DE_COMENTÁRIOS', blank=True, null=True)  # Field name made lowercase.
    numero_de_avaliações = models.IntegerField(db_column='NÚMERO_DE_AVALIAÇÕES', blank=True, null=True)  # Field name made lowercase.

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
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    DATA = models.DateField(db_column='DATA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Pedido = models.CharField(db_column='Pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Data_do_pedido = models.CharField(db_column='Data_do_pedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Avaliacao = models.CharField(db_column='Avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Data_da_avaliação = models.CharField(db_column='Data_da_avaliação', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Comentário = models.CharField(db_column='Comentário', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Unnamed_6 = models.CharField(db_column='Unnamed__6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja  = models.CharField(db_column='Loja', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avaliacao'
    def __str__(self):
        return self.Cliente

class lojas(models.Model):
    Cliente = models.CharField(db_column='Cliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Loja  = models.CharField(db_column='Lojas', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lojas'
    def __str__(self):
        return self.Cliente