from django.urls import path
from django.contrib.auth import views
from accounts import views as account_views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path('signup/', account_views.UserSignUpView.as_view(), name='signup'),
]