from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
	path('', views.Main.as_view(), name = 'main'),
	path('chat/', views.Chat.as_view(), name = 'chat'),
	path('accounts/loggin', views.ProjectLoginView.as_view(), name = 'loggin'),
	path('accounts/register', views.ProjectRegisterView.as_view(), name = 'register'),
	path('accounts/logout', views.ProjectLogoutView.as_view(), name = 'logout'),
	path('rooms/list', views.List_Rooms.as_view(), name = 'rooms_list'),
	path('rooms/new_room', views.Create_Room.as_view(), name = 'new_room'),
	path('rooms/<int:id>', views.Room_Chat.as_view(), name = 'room_chat'),
]