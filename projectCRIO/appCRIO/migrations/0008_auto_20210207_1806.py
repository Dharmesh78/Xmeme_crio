# Generated by Django 3.0.6 on 2021-02-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCRIO', '0007_auto_20210207_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='meme_url',
            field=models.URLField(max_length=500),
        ),
    ]