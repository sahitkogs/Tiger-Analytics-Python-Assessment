# Generated by Django 2.1.3 on 2020-08-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200828_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='flight_call',
            field=models.FileField(blank=True, null=True, upload_to='json/flight_call/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='light_levels',
            field=models.FileField(blank=True, null=True, upload_to='json/light_levels/'),
        ),
    ]