# Generated by Django 3.1.7 on 2022-09-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20220911_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='accountno',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='bankname',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ifsccode',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
