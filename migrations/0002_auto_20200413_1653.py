# Generated by Django 3.0.5 on 2020-04-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_care', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['last_name']},
        ),
    ]
