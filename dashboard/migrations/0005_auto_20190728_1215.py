# Generated by Django 2.2.3 on 2019-07-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, default='images/placeholderImage.png', upload_to='images/'),
        ),
    ]
