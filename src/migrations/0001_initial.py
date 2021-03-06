# Generated by Django 2.0 on 2017-12-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('age', models.CharField(max_length=300)),
                ('weight', models.CharField(max_length=300)),
                ('picture', models.ImageField(upload_to='templates/images/')),
            ],
        ),
    ]
