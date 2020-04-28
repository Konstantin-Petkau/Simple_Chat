from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
	path('', views.Main.as_view(), name = 'main'),
	path('chat/', views.Chat.as_view(), name = 'chat'),
	path('accounts/loggin/', views.ProjectLoginView.as_view(), name = 'loggin'),
	path('accounts/register/', views.ProjectRegisterView.as_view(), name = 'register'),
	path('accounts/logout', views.ProjectLogoutView.as_view(), name = 'logout'),
]