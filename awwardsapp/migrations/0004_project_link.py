# Generated by Django 3.1.2 on 2020-10-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0003_auto_20201023_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]