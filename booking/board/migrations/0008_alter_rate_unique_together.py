# Generated by Django 3.2.9 on 2021-11-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_seats_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('name', 'service')},
        ),
    ]
