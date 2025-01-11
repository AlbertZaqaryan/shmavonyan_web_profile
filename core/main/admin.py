from django.contrib import admin
from .models import Article, ContactMessage, Profile, About, Education, Experience, Awards, Science_visit
# Register your models here.

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(ContactMessage)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Awards)
admin.site.register(Science_visit)