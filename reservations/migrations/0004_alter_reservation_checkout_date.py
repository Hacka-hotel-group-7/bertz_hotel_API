# Generated by Django 4.2.7 on 2023-11-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
