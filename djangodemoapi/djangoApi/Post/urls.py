from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Api to add likepost with post method and get all likepost with get method
    url(r'^likepost/$',views.LikePostview.as_view(),name='likepost'),
    # Api to update and delete the likeposts
    url(r'^likepost/(?P<post_id>\d+)/$',views.LikePostview.as_view(),name='likepost'),
    # Api to add dislikepost with post method and get all dislikepost with get method    
    url(r'^dislikepost/$',views.DislikePostView.as_view(),name='dislikepost'),
    # Api to update and delete the dislikeposts    
    url(r'^dislikepost/(?P<post_id>\d+)/$',views.DislikePostView.as_view(),name='dislikepost'),

    url(r'add_favorite/$',views.AddFavorite.as_view(),name='add_favorite'),
    url(r'dislike_favorite/$',views.DislikeFav.as_view(),name='dislike_favorite'),

    url(r'^add_like/(?P<likepost_id>\d+)/(?P<dislikepost_id>\d+)/$',views.AddLike.as_view(),name='add_like'),
    url(r'^add_like/$',views.AddLike.as_view(),name='add_like'),
    
    url(r'^add_dislike/(?P<likepost_id>\d+)/(?P<dislikepost_id>\d+)/$',views.AddDislike.as_view(),name='add_dislike'),
    url(r'^add_dislike/$',views.AddDislike.as_view(),name='add_dislike'),
    
    url(r'^add_share/(?P<likepost_id>\d+)/(?P<dislikepost_id>\d+)/$',views.AddShare.as_view(),name='add_share'),
    url(r'^add_share/$',views.AddShare.as_view(),name='add_share'),
    
    url(r'^add_seen/(?P<likepost_id>\d+)/(?P<dislikepost_id>\d+)/$',views.AddSeen.as_view(),name='add_seen'),
    url(r'^add_seen/$',views.AddSeen.as_view(),name='add_seen'),
    
    url(r'^add_comment/(?P<likepost_id>\d+)/(?P<dislikepost_id>\d+)/$',views.AddComment.as_view(),name='add_comment'),
    url(r'^add_comment/$',views.AddComment.as_view(),name='add_comment'),
    
    url(r'^home/$',views.Home.as_view(),name='home'),
    url(r'^comments/(?P<id>\d+)/$',views.CommentsAPI.as_view(),name='home'),
    url(r'^dislikehome/$',views.HomeDislikePosts.as_view(),name='home'),
    # Api for getting the followers and following data
    url(r'^follow_details/$',views.FollowView.as_view(),name='follow_details'),
    url(r'^my_like_posts/$',views.MyLikePosts.as_view(),name='my_like_posts'),
    url(r'^my_dislike_posts/$',views.MyDisLikePosts.as_view(),name='my_dislike_posts'),
]