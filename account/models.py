# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """user model"""

    phone = models.CharField(max_length=255, blank=True, null=True)




