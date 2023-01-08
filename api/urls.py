from django.urls import path
from .views import BookReviewApiView, BookReviewAllAPIView


urlpatterns = [
    path("review/<int:pk>/", BookReviewApiView.as_view(), name='review_detail'),
    path("review/", BookReviewAllAPIView.as_view(), name='review_all'),

]