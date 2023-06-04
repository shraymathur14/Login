from django.db import models

# Create your models here.
class Signin(models.Model):
    Username = models.CharField(blank=False, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Username

class SignUp(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    mail = models.EmailField(blank=False)
    def __str__(self):
        return self.name