from django.contrib import admin
from .models import Article, Department, Comment, MostPopular

# Register your models here.
admin.site.register(Department)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(MostPopular)