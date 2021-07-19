# Generated by Django 3.1.2 on 2020-10-24 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwardsapp', '0006_auto_20201024_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('rate_design', models.PositiveSmallIntegerField(choices=[(1, '1-Dung'), (2, '2-Troll'), (3, '3-Awful'), (4, '4-Poor'), (5, '5-Average'), (6, '6-Barely Above Average'), (7, '7-Good'), (8, 'Excellent'), (9, 'Exceeds Expectations'), (10, '10-Outstanding')])),
                ('rate_usability', models.PositiveSmallIntegerField(choices=[(1, '1-Dung'), (2, '2-Troll'), (3, '3-Awful'), (4, '4-Poor'), (5, '5-Average'), (6, '6-Barely Above Average'), (7, '7-Good'), (8, 'Excellent'), (9, 'Exceeds Expectations'), (10, '10-Outstanding')])),
                ('rate_content', models.PositiveSmallIntegerField(choices=[(1, '1-Dung'), (2, '2-Troll'), (3, '3-Awful'), (4, '4-Poor'), (5, '5-Average'), (6, '6-Barely Above Average'), (7, '7-Good'), (8, 'Excellent'), (9, 'Exceeds Expectations'), (10, '10-Outstanding')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awwardsapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
