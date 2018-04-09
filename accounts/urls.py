from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.TopPageView.as_view(), name='index'),
    url(r'^mypage/$', views.MyPageView.as_view(), name='mypage'),
    #url(r'^create/$', views.create, name='create'),
    url(r'^login/$', views.logins, name='login'),
    #url(r'^logout/$', views.logouts, name='logout'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]