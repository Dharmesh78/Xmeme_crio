# Generated by Django 3.0.6 on 2021-02-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCRIO', '0006_auto_20210207_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='mid',
        ),
        migrations.AddField(
            model_name='meme',
            name='meme_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
