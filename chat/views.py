from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import Auth_Form, Register_Form, LetterForm, Create_Room_Form, Create_Letter_For_Room
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Letter, Rooms, Letter_For_Room
from django.contrib.auth.mixins import LoginRequiredMixin



class Main(TemplateView):
	template_name = 'main.html'


'''Форма для написания нового сообщения в чате '''
class Chat(LoginRequiredMixin, CreateView):
	template_name = 'chat.html'
	model = Letter
	form_class = LetterForm
	success_url = '/chat/'


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['letter'] = Letter.objects.all()
		return context


	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)


'''Контроллер-класс для входа в аккаунт пользователя '''
class ProjectLoginView(LoginView):
	template_name = 'accounts/loggin.html'
	form_class = Auth_Form
	success_url = '/chat/'
	

	def get_success_url(self):
		return self.success_url


'''Контроллер-класс для регистрации нового пользователя '''
class ProjectRegisterView(CreateView):
	model = User
	template_name = 'accounts/register.html'
	success_url = '/'
	form_class = Register_Form


'''Контроллер-класс для выхода из аккаунта '''
class ProjectLogoutView(LogoutView):
	next_page = '/'

'''Контроллер-класс для отобржения списка комнат '''
class List_Rooms(TemplateView):
	template_name = 'rooms/list_for_rooms.html'


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rooms'] = Rooms.objects.all()
		return context

'''Контроллер-класс для создания комнаты '''
class Create_Room(CreateView):
	model = Rooms
	form_class = Create_Room_Form
	success_url = '/rooms/list'
	template_name = 'rooms/create_new_room.html'


	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)

'''Контроллер-класс для сообщений в комнатах '''
class Room_Chat(LoginRequiredMixin, CreateView):
	template_name = 'rooms/room_chat.html'
	model = Letter_For_Room
	form_class = Create_Letter_For_Room
	success_url = '/rooms/list'


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['letter'] = Letter_For_Room.objects.filter(room = Rooms.objects.get(id =  self.kwargs['id']))
		return context


	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.author = self.request.user
		self.object.room = Rooms.objects.get(id =  self.kwargs['id'])
		self.object.save()
		return super().form_valid(form)