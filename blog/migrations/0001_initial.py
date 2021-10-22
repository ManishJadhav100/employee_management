# Generated by Django 3.1.2 on 2021-10-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('job', models.CharField(max_length=250)),
                ('salary', models.BigIntegerField(null=True)),
            ],
        ),
    ]