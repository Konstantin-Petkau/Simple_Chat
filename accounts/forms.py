from django.forms import ModelForm
from .models import Account


'''форма для регистрации пользователя '''
class Register_Form(ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'password', 'email']