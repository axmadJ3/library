from rest_framework.routers import DefaultRouter

from .views import BookViewSet, AuthorViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls
