# Generated by Django 4.2.7 on 2023-11-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='loan',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
