# Generated by Django 4.0 on 2022-02-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customusermodel_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='role',
            field=models.BooleanField(default=False),
        ),
    ]
