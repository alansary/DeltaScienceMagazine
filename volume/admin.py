from django.contrib import admin
from .models import Year, Volume, Paper, Highlight, Author, MostPopularPaper

# Register your models here.
admin.site.register(Year)
admin.site.register(Volume)
admin.site.register(Paper)
admin.site.register(Highlight)
admin.site.register(Author)
admin.site.register(MostPopularPaper)