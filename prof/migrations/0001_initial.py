# Generated by Django 3.0.4 on 2020-05-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.IntegerField(max_length=9)),
                ('password', models.TextField(max_length=64)),
            ],
        ),
    ]
