from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
	path('', views.Main.as_view(), name = 'main'),
	path('accounts/loggin/', views.ProjectLoginView.as_view(), name = 'loggin'),
	path('accounts/register/', views.ProjectRegisterView.as_view(), name = 'register'),
]