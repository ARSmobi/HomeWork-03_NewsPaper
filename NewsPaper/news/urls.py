from django.urls import path
from .views import (PostList, PostDetail, PostCreate, PostUpdate, PostDelete,
                    subscriptions)

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/search/', PostList.as_view(), name='search'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
