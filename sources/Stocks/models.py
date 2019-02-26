from django.db import models

# Create your models here.
from django.utils.text import slugify


class Marque(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    slug = models.SlugField(unique=True, default="", blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Marque, self).save(*args, **kwargs)


class Categorie(models.Model):
    name = models.CharField(max_length=255, verbose_name="Catégorie")
    description = models.TextField(default="", blank=True)
    slug = models.SlugField(unique=True, default="", blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categorie, self).save(*args, **kwargs)


class Element(models.Model):
    OK = 1
    KO = 2
    REPARATION = 3
    INCONNU = 4
    OUTDATED = 5

    STATE_CHOICES = (
        (OK, 'Bon état'),
        (KO, 'Pour pièces'),
        (REPARATION, 'En réparation'),
        (INCONNU, 'Inconnu'),
        (OUTDATED, 'Usagé'),
    )

    name = models.CharField(max_length=255, verbose_name="Nom")
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, verbose_name="Marque", null=True, blank=True)
    model = models.CharField(max_length=255, verbose_name="Modèle", blank=True)
    description = models.TextField(default="", blank=True)
    count = models.IntegerField(verbose_name="Quantité", default=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, verbose_name="Catégorie", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Prix", default=0)
    caution = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Caution", default=0)
    image = models.ImageField(verbose_name="Image", null=True, blank=True)
    slug = models.SlugField(unique=True, default="", blank=True, editable=False)
    state = models.PositiveSmallIntegerField(choices=STATE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Element, self).save(*args, **kwargs)
