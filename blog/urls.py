from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    # path('videos',views.VideoListView.as_view(),name='videos'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.update_post, name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment')
]

