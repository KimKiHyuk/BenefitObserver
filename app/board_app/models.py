from django.db import models

# Create your models here.
class PostManager(models.Manager):
    def with_url_all(self):
        pass

class Posts(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    url = models.ForeignKey('board_app.Url', on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['updated_at']

class Url(models.Model):
    objects = models.Manager()
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'Urls'