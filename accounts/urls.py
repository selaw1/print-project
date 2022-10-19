from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from accounts import views



translatable_urlpatterns = i18n_patterns(
    # Home
    path('', views.HomeView.as_view(), name="home"),
    # Authentication 
    path('registration/', views.UserCreateView.as_view() ,name='create-user'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/registration/login.html', 
        redirect_authenticated_user=True), 
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/login/'), 
        name='logout'),
)
