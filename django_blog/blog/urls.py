from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet

router = SimpleRouter()
router.register('articles', ArticleViewSet)

urlpatterns = router.urls
