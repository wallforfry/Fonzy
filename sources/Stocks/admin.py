from django.contrib import admin

# Register your models here.
from Stocks.models import Categorie, Element

admin.site.register(Categorie)
admin.site.register(Element)