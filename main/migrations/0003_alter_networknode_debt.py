# Generated by Django 5.0.1 on 2024-01-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_networknode_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknode',
            name='debt',
            field=models.FloatField(default=None, verbose_name='задолженность'),
        ),
    ]