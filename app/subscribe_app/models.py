from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Subscribe(models.Model):
    class Topic(models.TextChoices):
        SWDEPT = 'Software engineering', _('소프트웨어 융합대학')
        NSDEPT = 'Natural science', _('자연과학대학')

    objects = models.Manager()
    user = models.ForeignKey("auth_app.User", on_delete=models.CASCADE, blank=False)
    topic = models.CharField(
        max_length=30,
        choices=Topic.choices,
        default=Topic.SWDEPT,
    )
    

    def __str__(self):
        return str(f'{self.user} | {self.topic}')
    
    class Meta:
        verbose_name_plural = 'Subscribe'