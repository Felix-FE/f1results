# Generated by Django 3.2.9 on 2021-11-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeEntry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='year',
            field=models.CharField(default=2021, max_length=200),
            preserve_default=False,
        ),
    ]
