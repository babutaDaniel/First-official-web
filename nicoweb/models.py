from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(default=datetime.now)
    category = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=30)
    upload_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title + '  :  ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article', args=(str(self.id)) )    pagina cu postarea
        return reverse('home')
    
    #@property
    #def Days_posted(self):
        #today = date.today()
        #days = self.post_date.date()
        #days_scripped = str(days).split(",",1)[0]
       # return 41

