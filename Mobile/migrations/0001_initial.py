# Generated by Django 4.0 on 2021-12-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('JAN_Code', models.CharField(max_length=200, unique=True)),
                ('Image', models.TextField()),
            ],
        ),
    ]