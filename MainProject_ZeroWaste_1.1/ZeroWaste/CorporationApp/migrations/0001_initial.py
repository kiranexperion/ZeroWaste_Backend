# Generated by Django 3.2.16 on 2022-11-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wastes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_type', models.CharField(max_length=200)),
                ('charge', models.FloatField()),
            ],
        ),
    ]