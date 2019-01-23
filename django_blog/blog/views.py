# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import ReadOnly
from .serializer import ArticleSerializer, Article


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticated | ReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
