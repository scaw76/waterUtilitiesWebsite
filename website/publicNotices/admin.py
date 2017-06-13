from django.contrib import admin
from .models import Notice, NoticeFile

# Register your models here.

class FilesInline(admin.StackedInline):
	model = NoticeFile

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title_text', 'pub_date')
	inlines = (FilesInline,)


admin.site.register(Notice, NoticeAdmin)

