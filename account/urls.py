from django.urls import include, path
from knox import views as knox_views
from .api import RegisterAPI, LoginAPI, UserAPI, UsersAPI, UpdateUserAPI, ChangePasswordView, UsernameRetrieveAPIView


urlpatterns = [
    path('api/auth', include('knox.urls'), name='knox'),
    path('api/auth/register', RegisterAPI.as_view(), name='user_register'),
    path('api/auth/login', LoginAPI.as_view(), name='user_login'),
    path('api/auth/user/<int:pk>/', UserAPI.as_view(), name='user_raudal'),
    path('api/auth/user/<str:username>/', UsernameRetrieveAPIView.as_view(), name='username_raudal'),
    path('api/auth/update/<int:pk>/', UpdateUserAPI.as_view(), name='user_update_raudal'),
    path('api/auth/users', UsersAPI.as_view(), name='users_raudal'),
    path('api/auth/changepassword/<int:pk>', ChangePasswordView.as_view(), name='change_password'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
