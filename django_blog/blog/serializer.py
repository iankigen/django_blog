from django.urls import reverse
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title',
                  'body',
                  'user_id',
                  'url',
                  'created_date',
                  'modified_date')

    def get_user_id(self, obj):

        return str(obj.user.id)

    def get_url(self, obj):
        return reverse('article-detail', kwargs={'pk': obj.id})

