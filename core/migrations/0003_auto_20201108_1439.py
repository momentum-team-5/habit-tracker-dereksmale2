# Generated by Django 3.1.3 on 2020-11-08 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_habit_record'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('habit', 'date_completed')},
        ),
    ]