# Generated by Django 2.0.2 on 2018-03-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_article_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
