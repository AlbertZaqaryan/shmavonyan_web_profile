from django.contrib import admin
from .models import Article, ContactMessage, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(ContactMessage)