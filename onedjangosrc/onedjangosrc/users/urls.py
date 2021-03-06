from django.contrib.auth import views as auth_views
from django.urls import path
from .views import LoginView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
