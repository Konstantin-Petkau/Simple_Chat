from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Account
from .forms import Register_Form
from django.urls import reverse_lazy


'''контроллер-класс для регистрации нового пользователя '''
class Register(CreateView):
	model = Account
	template_name = 'accounts/register.html'
	form_class = Register_Form
	success_url = '/'