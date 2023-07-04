from django.urls import path
from .views import HomePageView, CreatePostView


urlpatterns = [
    path('', HomePageView.as_view(), name='posts'),
    path('post/', CreatePostView.as_view(), name='post'),
]
