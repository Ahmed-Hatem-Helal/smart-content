# Generated by Django 4.1.1 on 2022-09-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_article_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='first_image',
            field=models.ImageField(blank=True, upload_to='uploads/photos/'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='second_image',
            field=models.ImageField(blank=True, upload_to='uploads/photos/'),
        ),
    ]
