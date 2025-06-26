from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admision/', views.admision, name='admision'),
    path('niveles/', views.niveles, name='niveles'),
    path('psicologia/', views.psicologia, name='psicologia'),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    #Login
    path('psicologia/login/', views.login_view, name='login'),
    path('psicologia/portada/', views.portada, name='portada'),
    path('psicologia/logout/', views.logout_view, name='logout'),
    path('psicologia/register/', views.register, name='register'),
    path('psicologia/test-beck/', views.test_beck, name='test_beck'),

]
