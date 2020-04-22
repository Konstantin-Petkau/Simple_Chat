from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Letter


'''Форма для входа в аккаунт пользователя '''
class Auth_Form(AuthenticationForm, ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


'''Форма для регистрации нового пользователя '''
class Register_Form(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class LetterForm(ModelForm):
	class Meta:
		model = Letter
		fields = ['text']
	