from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'dashboard/', views.dashboard, name='dashboard'),
    url(r'TestBedSetup/', views.testbed,name= 'testbed'),
    url(r'save/', views.save, name='save'),
    url(r'preview/', views.preview, name='preview'),
    url(r'testbedmodify/', login_required(views.tb_modify), name='tb_modify'),
    url(r'delete/', views.delete, name='delete'),
    url(r'execution/', views.execution, name='execution'),
    url(r'change_pswd/', views.change_pswd, name='change_pswd'),
    url(r'changepswd/', views.changepswd, name='changepswd'),
    url(r'history/', views.history, name='history'),
    url(r'testmetrics/', views.testmetrics, name='testmetrics'),
    url(r'export_users_xls/',views.export_data,name='export_data'),
]
