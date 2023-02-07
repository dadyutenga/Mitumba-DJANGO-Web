# Generated by Django 4.1.3 on 2022-12-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_notes',
            field=models.TextField(blank=True, default='order notes', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='e.g 2547 1234 5678', max_length=15),
        ),
    ]
