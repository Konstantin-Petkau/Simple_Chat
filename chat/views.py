from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import Auth_Form, Register_Form
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class Main(TemplateView):
	template_name = 'main.html'


'''Контроллер-класс для входа в аккаунт пользователя '''
class ProjectLoginView(LoginView):
	template_name = 'accounts/loggin.html'
	form_class = Auth_Form
	success_url = '/'


'''Контроллер-класс для регистрации нового пользователя '''
class ProjectRegisterView(CreateView):
	model = User
	template_name = 'accounts/register.html'
	success_url = '/'
	form_class = Register_Form
