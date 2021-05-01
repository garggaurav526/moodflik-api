from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    url(r'^create_likepost/$',views.CreateLikePost.as_view(),name='create_likepost'),
    url(r'^create_dislikepost/$',views.CreateDislikePost.as_view(),name='create_dislikepost'),

]