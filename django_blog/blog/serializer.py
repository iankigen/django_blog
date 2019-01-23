from django.urls import reverse
from rest_framework import serializers

from .models import Article

from users.serializer import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'user',
            'created_date',
            'modified_date')
