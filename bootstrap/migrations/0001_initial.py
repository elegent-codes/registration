# Generated by Django 3.2.7 on 2021-09-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formModel',
            fields=[
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
