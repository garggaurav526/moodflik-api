from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Api to add likepost with post method and get all likepost with get method
    url(r'^likepost/$',views.LikePostview.as_view(),name='likepost'),
    # Api to update and delete the likeposts
    url(r'^likepost/(?P<user_id>\d+)/$',views.LikePostview.as_view(),name='likepost'),
    # Api to add dislikepost with post method and get all dislikepost with get method    
    url(r'^dislikepost/$',views.DislikePostView.as_view(),name='dislikepost'),
    # Api to update and delete the dislikeposts    
    url(r'^dislikepost/(?P<user_id>\d+)/$',views.DislikePostView.as_view(),name='dislikepost'),
    # these are the api to add reactions and add_favorite get method will get the favorites post and 
        # post method will help to add post to favorites
    url(r'add_favorite/$',views.AddFavorite.as_view(),name='add_favorite'),
    url(r'^add_like/$',views.AddLike.as_view(),name='add_like'),
    url(r'^add_dislike/$',views.AddDislike.as_view(),name='add_dislike'),
    url(r'^add_share/$',views.AddShare.as_view(),name='add_share'),
    url(r'^add_seen/$',views.AddSeen.as_view(),name='add_seen'),
    url(r'^add_comment/$',views.AddComment.as_view(),name='add_comment'),
    url(r'^home/$',views.Home.as_view(),name='home'),
    # Api for getting the followers and following data
    url(r'^follow_details/$',views.FollowView.as_view(),name='follow_details'),
]