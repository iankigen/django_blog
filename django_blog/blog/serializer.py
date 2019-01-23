from django.urls import reverse
from rest_framework import serializers

from .models import Article

from users.serializer import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title',
                  'body',
                  'user',
                  'url',
                  'created_date',
                  'modified_date')


    def get_url(self, obj):
        return reverse('article-detail', kwargs={'pk': obj.id})

