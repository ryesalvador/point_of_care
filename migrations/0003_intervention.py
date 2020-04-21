# Generated by Django 3.0.5 on 2020-04-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_care', '0002_auto_20200413_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervention', models.CharField(max_length=175)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['intervention'],
            },
        ),
    ]
