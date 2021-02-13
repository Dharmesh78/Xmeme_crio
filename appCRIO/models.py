from django.db import models

# Create your models here.
class Meme(models.Model):
    #id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=256,null=True)
    caption=models.CharField(max_length=256)
    url=models.URLField(max_length=500)

    def __str__(self):
        return self.name
