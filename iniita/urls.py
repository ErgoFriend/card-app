from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^create/$',views.create,name='create'),
    url(r'^mypage/$',views.mypage,name='mypage'),
    url(r'^test/$',views.test,name='test'),
    url(r'^([0-9]+)/$',views.detail,name='detail'),
    url(r'^([0-9]+)/update/$',views.update,name='update'),
    url(r'^([0-9]+)/delete/$',views.delete,name='delete'),
    #url(r'login/$',views.login,name='login'),
    #url(r'iniita/user/(\s+)/$',views.user,name='user'),
] 