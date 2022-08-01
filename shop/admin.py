from django.contrib import admin

from .models import Category, Product, Comment, Rating, Like

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
