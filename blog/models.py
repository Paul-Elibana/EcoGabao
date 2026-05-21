from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image_couverture = models.ImageField(upload_to='blog/', blank=True)
    publie = models.BooleanField(default=True)
    vues = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre

