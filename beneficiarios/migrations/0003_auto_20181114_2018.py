# Generated by Django 2.1.1 on 2018-11-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0002_beneficiarios_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiarios',
            name='observacion',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
