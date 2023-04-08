from django.contrib import admin
from ckeditor.fields import RichTextField

content = RichTextField(blank=True, null=True)

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'slug', 'status', 'created_on')
  list_filter = ('status',)
  search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)