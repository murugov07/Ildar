from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.main_page, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path('accounts/profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('reset_password/', views.reset, name='reset'),
    path('reset_password/<str:mail>', views.reset_2, name='reset_2'),
    path('password-change/', views.change_password, name='password_change'),
    path('api/answer/', views.answer, name='answer'),
    path('support/', views.support, name='support')
]