# Generated by Django 4.1.1 on 2022-09-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_article_paragraph_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
