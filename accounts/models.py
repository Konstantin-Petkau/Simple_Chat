from django.db import models


'''модель для аккаунтов '''
class Account(models.Model):
	name = models.CharField(max_length = 50, unique = True, verbose_name = 'Аккаунт')
	password = models.CharField(max_length = 100, unique = True, verbose_name = 'Пароль')
	email = models.EmailField(max_length = 254, unique = True, verbose_name = 'Электронная почта')


	class Meta:
		verbose_name = 'Аккаунт'
		verbose_name_plural = 'Аккаунты'


	def __str__(self):
		return self.name