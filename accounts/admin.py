from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

UserAdmin.fieldsets[0][1]['fields'] = ['phone','Image','address','Techer']

admin.site.register(User,UserAdmin)