from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()
    
    reporter = models.CharField(max_length=150)
    #reporter = models.ForeignKey(User)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.id})
