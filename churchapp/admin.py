from django.contrib import admin
from . models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

admin.site.register(User, UserAdmin)
admin.site.register(Messages)
# admin.site.register(Notices)

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'date', 'varify']

admin.site.register(Notices, NoticeAdmin)



