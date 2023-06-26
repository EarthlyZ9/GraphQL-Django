from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=64, unique=True, null=False)
    name = models.CharField(max_length=10, null=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
