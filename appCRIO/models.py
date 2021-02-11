from django.db import models

# Create your models here.
class Meme(models.Model):
    meme_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=256,null=True)
    mcaption=models.CharField(max_length=256)
    meme_url=models.URLField(max_length=500)

    def __str__(self):
        return self.name
