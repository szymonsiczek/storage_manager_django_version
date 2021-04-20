from django.contrib import admin
from .models import Item
from django.contrib.auth import get_user_model

admin.site.register(Item)
admin.site.register(get_user_model())
