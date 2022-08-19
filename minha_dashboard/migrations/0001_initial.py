# Generated by Django 4.0.6 on 2022-08-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NC_FINANCEIRO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, db_column='CLIENTE', max_length=255, null=True)),
                ('restaurante', models.CharField(blank=True, db_column='RESTAURANTE', max_length=255, null=True)),
                ('data', models.DateField(blank=True, db_column='DATA', null=True)),
                ('mes', models.IntegerField(blank=True, db_column='MES', null=True)),
                ('ano', models.IntegerField(blank=True, db_column='ANO', null=True)),
                ('dia', models.IntegerField(blank=True, db_column='DIA', null=True)),
                ('total_do_pedido', models.FloatField(blank=True, db_column='TOTAL_DO_PEDIDO', null=True)),
                ('valor_dos_itens', models.FloatField(blank=True, db_column='VALOR_DOS_ITENS', null=True)),
                ('incentivo_ifood', models.CharField(blank=True, db_column='INCENTIVO_IFOOD', max_length=255, null=True)),
                ('incentivo_loja', models.FloatField(blank=True, db_column='INCENTIVO_LOJA', null=True)),
                ('faturamento_liquido', models.IntegerField(blank=True, db_column='FATURAMENTO_LIQUIDO', null=True)),
                ('valor_de_taxa_de_transacao', models.FloatField(blank=True, db_column='VALOR_DE_TAXA_DE_TRANSACAO', null=True)),
                ('valor_de_taxa_de_1_semana', models.FloatField(blank=True, db_column='VALOR_DE_TAXA_DE_1_SEMANA', null=True)),
                ('numero_de_pedidos', models.IntegerField(blank=True, db_column='NUMERO_DE_PEDIDOS', null=True)),
                ('numero_de_cancelamentos', models.IntegerField(blank=True, db_column='NUMERO_DE_CANCELAMENTOS', null=True)),
                ('valor_bruto_cancelado_na_plataforma', models.IntegerField(blank=True, db_column='VALOR_BRUTO_CANCELADO_NA_PLATAFORMA', null=True)),
                ('valor_liquido_cancelado_na_plataforma', models.IntegerField(blank=True, db_column='VALOR_LIQUIDO_CANCELADO_NA_PLATAFORMA', null=True)),
                ('taxa_de_entrega', models.FloatField(blank=True, db_column='TAXA_DE_ENTREGA', null=True)),
                ('faturamento_bruto', models.FloatField(blank=True, db_column='FATURAMENTO_BRUTO', null=True)),
                ('cancelamento_percent', models.FloatField(blank=True, db_column='CANCELAMENTO_PERCENT', null=True)),
                ('cancelamento_pelo_cliente', models.IntegerField(blank=True, db_column='CANCELAMENTO_PELO_CLIENTE', null=True)),
                ('cancelamento_pelo_cliente_percent', models.FloatField(blank=True, db_column='CANCELAMENTO_PELO_CLIENTE_PERCENT', null=True)),
                ('cancelamento_pelo_restaurante', models.IntegerField(blank=True, db_column='CANCELAMENTO_PELO_RESTAURANTE', null=True)),
                ('cancelamento_pelo_restaurante_percent', models.FloatField(blank=True, db_column='CANCELAMENTO_PELO_RESTAURANTE_PERCENT', null=True)),
                ('faturamento_real', models.FloatField(blank=True, db_column='FATURAMENTO_REAL', null=True)),
                ('ticket_medio', models.FloatField(blank=True, db_column='TICKET_MEDIO', null=True)),
                ('ticket_medio_real', models.FloatField(blank=True, db_column='TICKET_MEDIO_REAL', null=True)),
                ('incentivo_percent', models.FloatField(blank=True, db_column='INCENTIVO_PERCENT', null=True)),
                ('taxa_efetiva', models.FloatField(blank=True, db_column='TAXA_EFETIVA', null=True)),
                ('margem', models.FloatField(blank=True, db_column='MARGEM', null=True)),
                ('taxa_de_cancelamento', models.FloatField(blank=True, db_column='TAXA_DE_CANCELAMENTO', null=True)),
            ],
            options={
                'db_table': 'NC_FINANCEIRO',
                'managed': False,
            },
        ),
    ]