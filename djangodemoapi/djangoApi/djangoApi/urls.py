from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^User/', include('User.urls')),

    url(r'^post/', include('Post.urls')),
]
