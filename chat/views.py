from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import Auth_Form, Register_Form, LetterForm
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Letter



class Main(TemplateView):
	template_name = 'main.html'


class Chat(CreateView):
	template_name = 'chat.html'
	model = Letter
	form_class = LetterForm
	success_url = '/chat/'


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
