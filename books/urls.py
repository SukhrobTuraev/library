from rest_framework.routers import SimpleRouter
from .views import (
    BookListApiView, BookDetailApiView, BookDeleteApiView,
    BookUpdateApiView, BookCreateApiView, BookListCreateApiView,
    BookDetailUpdateDeleteApiView, BookViewSet
)
from django.urls import path

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('book/', BookListCreateApiView.as_view()),
    # path('book/<int:pk>/rud/', BookDetailUpdateDeleteApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view())
]
urlpatterns = urlpatterns + router.urls

# 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