from django.contrib import admin
from .models import Game, Review, Store

# Register your models here.
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Store)