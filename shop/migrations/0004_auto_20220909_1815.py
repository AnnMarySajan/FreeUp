# Generated by Django 3.1.7 on 2022-09-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_subcat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcat',
            name='catname',
        ),
        migrations.RemoveField(
            model_name='subcat',
            name='subcatname',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='subcat',
        ),
    ]