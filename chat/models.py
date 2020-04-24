from django.db import models
from django.contrib.auth.models import User


'''Модель для сообщений в чате '''
class Letter(models.Model):
	text = models.TextField(max_length = 600, verbose_name = 'Текст')
	author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
	date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата написания сообщения')


	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'
		ordering = ['-date']


	def __str__(self):
		return str(self.date)