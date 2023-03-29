from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import admin as auth_admin


from .models import User
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)
# Register your models here.

admin.site.register(User)