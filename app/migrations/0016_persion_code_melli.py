# Generated by Django 4.2.1 on 2023-05-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_persion_code_melli'),
    ]

    operations = [
        migrations.AddField(
            model_name='persion',
            name='code_melli',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
