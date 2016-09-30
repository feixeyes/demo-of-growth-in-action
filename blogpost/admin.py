from django.contrib import admin
from blogpost.models import Blogpost


class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title', 'author',)}

admin.site.register(Blogpost, BlogpostAdmin)
