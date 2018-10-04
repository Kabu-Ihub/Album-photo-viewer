from django.db import models
from django.urls import reverse
class Photos(models.Model):
  title = models.CharField(max_length=255,blank=True)
  ImagePhoto = models.ImageField(upload_to="media/",blank=True)
  Description = models.TextField(max_length=500,blank=True)
  
  

  def __str__(self):
    return self.title
  def get_absolute_url(self):
    return reverse("detail" , kwargs={"id":self.id})

