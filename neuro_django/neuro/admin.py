from django.contrib import admin
from .models import Tag, Post
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Tag)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post)
