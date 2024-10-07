from django.db import models
from django.contrib.auth.models import User

class Bien(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    est_admin = models.BooleanField(default=False)