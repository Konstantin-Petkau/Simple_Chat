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

'''Модель для комнат'''
class Rooms(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
	name = models.CharField(max_length = 100, verbose_name = 'Название')
	date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата содания')


	class Meta:
		verbose_name = 'Комната'
		verbose_name_plural = 'Комнаты'
		ordering = ['-date']


	def __str__(self):
		return str(self.name)

'''Модель для сообщений в комнатах '''
class Letter_For_Room(models.Model):
	text = models.TextField(max_length = 600, verbose_name = 'Текст')
	author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
	date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата написания сообщения')
	room = models.ForeignKey(Rooms, on_delete = models.CASCADE, verbose_name = 'Комната', null = True)


	class Meta:
		verbose_name = 'Сообщение для комнаты'
		verbose_name_plural = 'Сообщения для комнат'
		ordering = ['-date']


	def __str__(self):
		return str(self.date)