from django.contrib import admin

# Register your models here.
from Stocks.models import Categorie, Element, Marque

admin.site.register(Categorie)
admin.site.register(Element)
admin.site.register(Marque)