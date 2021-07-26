from django.urls import include, path
from knox import views as knox_views
from .api import RegisterAPI, LoginAPI, UserAPI


urlpatterns = [
    path('api/auth', include('knox.urls'), name='knox'),
    path('api/auth/register', RegisterAPI.as_view(), name='user_register'),
    path('api/auth/login', LoginAPI.as_view(), name='user_login'),
    path('api/auth/user', UserAPI.as_view(), name='user_raudal'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]