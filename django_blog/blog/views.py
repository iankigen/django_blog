# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializer import ArticleSerializer, Article
from .permissions import IsAuthenticatedAndOwner


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateArticleViewSet(ArticleViewSet):
    permission_classes = (IsAuthenticatedAndOwner,)
    http_method_names = ['get', 'patch', 'put', 'delete']
