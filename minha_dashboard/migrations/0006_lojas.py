# Generated by Django 4.0.6 on 2022-08-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0005_avaliacao_promocao_tempo'),
    ]

    operations = [
        migrations.CreateModel(
            name='lojas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(blank=True, db_column='Cliente', max_length=255, null=True)),
                ('Loja', models.CharField(blank=True, db_column='Lojas', max_length=255, null=True)),
            ],
            options={
                'db_table': 'lojas',
                'managed': False,
            },
        ),
    ]
