# Generated by Django 4.1.3 on 2023-01-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_newslettersubscriber_delete_newsletterubscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='brand/images')),
            ],
        ),
    ]
