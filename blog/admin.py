from django.contrib import admin
from blog.models import Post, Theme

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	pass
	
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
	pass