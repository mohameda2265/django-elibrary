# Generated by Django 3.0.6 on 2020-06-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200609_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default='book_image/default.png', upload_to='project/book/static/images/'),
        ),
    ]