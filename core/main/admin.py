from django.contrib import admin
from .models import Article, ContactMessage, Profile, About, Education
# Register your models here.

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(ContactMessage)
admin.site.register(About)
admin.site.register(Education)