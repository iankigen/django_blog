from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, UpdateArticleViewSet

router = SimpleRouter()
router.register('articles', ArticleViewSet)
router.register('update-articles', UpdateArticleViewSet)

urlpatterns = router.urls
