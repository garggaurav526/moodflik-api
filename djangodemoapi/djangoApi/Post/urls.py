from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^show_likepost/$',views.LikePostview.as_view(),name='show_likepost'),
    url(r'^create_likepost/$',views.LikePostview.as_view(),name='create_likepost'),
    url(r'^show_dislikepost/$',views.DislikePostView.as_view(),name='show_dislikepost'),
    url(r'^create_dislikepost/$',views.DislikePostView.as_view(),name='create_dislikepost'),
    url(r'^add_favorite/$',views.AddFavorite.as_view(),name='add_favorite'),
    url(r'^add_like/$',views.AddLike.as_view(),name='add_like'),
    url(r'^add_dislike/$',views.AddDislike.as_view(),name='add_dislike'),
    url(r'^add_share/$',views.AddShare.as_view(),name='add_share'),
    url(r'^add_seen/$',views.AddSeen.as_view(),name='add_seen'),
    url(r'^add_comment/$',views.AddComment.as_view(),name='add_comment'),
    url(r'^home/$',views.Home.as_view(),name='home'),
]