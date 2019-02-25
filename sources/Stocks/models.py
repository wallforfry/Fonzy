from django.db import models


# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=255, verbose_name="Catégorie")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    description = models.TextField(default="", blank=True)
    count = models.IntegerField(verbose_name="Quantité", default=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, verbose_name="Catégorie", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Prix", default=0)
    caution = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Caution", default=0)
    image = models.ImageField(verbose_name="Image", null=True, blank=True)

    def __str__(self):
        return self.name