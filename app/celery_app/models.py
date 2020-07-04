from django.db import models

# Create your models here.

class CrawlerTask(models.Model):
    log = models.TextField()
    done_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.done_at)
    
    class Meta:
        verbose_name_plural = 'CrawlerTask'