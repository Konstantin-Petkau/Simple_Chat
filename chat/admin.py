from django.contrib import admin
from .models import Letter, Rooms, Letter_For_Room


admin.site.register(Letter)
admin.site.register(Rooms)
admin.site.register(Letter_For_Room)