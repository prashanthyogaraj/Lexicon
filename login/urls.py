from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_intra, name='login'),
    url(r'^\/', views.logout_intra, name='login'),
    url(r'^admin_home/$', views.admin_home, name='admin'),
    url(r'^validate/$', views.validate, name='validate'),
]
