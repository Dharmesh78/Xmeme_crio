# Generated by Django 3.0.6 on 2021-02-07 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appCRIO', '0002_auto_20210205_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='id',
        ),
        migrations.AddField(
            model_name='meme',
            name='mcaption',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meme',
            name='mid',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meme',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
