# Generated by Django 3.1.7 on 2022-09-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brandname',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='payment',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
