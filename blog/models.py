from django.db import models
from django.urls import reverse
# Create your models here.

# Columns: title, author (linked to users), body

class Post(models.Model):                       # our Table Name = appname_modelname blog_post
    title = models.CharField(max_length=200)    # Column 1
    author = models.ForeignKey(                 # Column 2
        'auth.User',
        on_delete = models.CASCADE
    )
    body = models.TextField()                   # Column 3

    def __str__(self):
        return self.title

    def get_absolute_url(self):                 # After succss of post_new this url is the default url the page should go to       
        # reverse loads the path from urls.py based on template name: 
        # path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),     j             
        return reverse('post_detail', args=[str(self.id)])