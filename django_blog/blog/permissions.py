from rest_framework.permissions import BasePermission

from .models import Article


class IsAuthenticatedAndOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            print('---->', 'request.user.is_authenticated', request.user.is_authenticated)
            article = Article.objects.get(pk=view.kwargs['pk'])
            print('====>', article.user.id == request.user.id)
            print('====>', article.user.id , request.user.id)
            return False if not article else article.user.id == request.user.id
        return False
