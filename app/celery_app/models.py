from django.db import models

# Create your models here.

class CrawlerTask(models.Model):
    objects = models.Manager()
    log = models.TextField()
    done_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.done_at)
    
    class Meta:
        ordering =['done_at']
        verbose_name_plural = 'CrawlerTask'
