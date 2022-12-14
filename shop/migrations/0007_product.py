# Generated by Django 3.1.7 on 2022-09-11 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_subcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prname', models.CharField(max_length=100)),
                ('catname1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('subcat1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('img', models.ImageField(upload_to='pics')),
                ('statename1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('cityname1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('praddress', models.TextField()),
                ('desc', models.TextField()),
                ('dop', models.DateField()),
                ('price', models.IntegerField()),
                ('payment', models.IntegerField(blank=True, default=None, null=True)),
                ('verifystatus', models.BooleanField(default=False)),
                ('activestatus', models.BooleanField(default=True)),
                ('catname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
                ('cityname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.city')),
                ('statename', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.state')),
                ('subcatname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.subcat')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
