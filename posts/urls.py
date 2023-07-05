from django.urls import path
from .views import HomePageView, CreatePostView, UpdatePostView


urlpatterns = [
    path('', HomePageView.as_view(), name='posts'),
    path('post/', CreatePostView.as_view(), name='post'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
]
