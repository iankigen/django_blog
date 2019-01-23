# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "Article: {}".format(self.title)
