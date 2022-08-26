# Generated by Django 4.1 on 2022-08-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0006_lojas'),
    ]

    operations = [
        migrations.CreateModel(
            name='promocoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, db_column='cliente', max_length=255, null=True)),
                ('promoção', models.CharField(blank=True, db_column='promoção', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='status', max_length=255, null=True)),
                ('data', models.DateField(blank=True, db_column='data', max_length=255, null=True)),
                ('loja', models.CharField(blank=True, db_column='loja', max_length=255, null=True)),
                ('hora', models.CharField(blank=True, db_column='hora', max_length=255, null=True)),
            ],
            options={
                'db_table': 'promocoes',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='promocao',
        ),
    ]
