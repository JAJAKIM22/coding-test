from django.db import models

# Create your models here.



class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_body = models.CharField(max_length=2000)


