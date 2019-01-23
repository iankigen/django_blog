# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

