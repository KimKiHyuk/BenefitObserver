from django.db import models

# Create your models here.

class Auth(models.Model):
    obejcts = models.Manager()
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name_plural = 'Auth'
        ordering = ['updated_at']
