from django.db import models
from django.contrib.auth.models import User


class UserAuth(User):
    created = models.DateTimeField(auto_now_add=True)
