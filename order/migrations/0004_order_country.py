# Generated by Django 4.1.3 on 2022-12-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_order_notes_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='Your nation/state/country', max_length=100),
        ),
    ]