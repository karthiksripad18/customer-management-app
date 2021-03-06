# Generated by Django 3.0.8 on 2020-07-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200711_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True),
        ),
    ]
