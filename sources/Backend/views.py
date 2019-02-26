from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Stocks.models import Element, Categorie, Marque


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def list_elements(request):
    elements = Element.objects.all()
    return render(request, "elements/list_elements.html", context={"elements": elements})

@login_required
def list_elements_in_categorie(request, slug):
    elements = Element.objects.filter(categorie__slug=slug).all()
    categorie = Categorie.objects.get(slug=slug)
    return render(request, "elements/list_elements.html", context={"elements": elements, "categorie": categorie})

@login_required
def list_elements_in_brand(request, slug):
    elements = Element.objects.filter(marque__slug=slug).all()
    marque = Marque.objects.get(slug=slug)
    return render(request, "elements/list_elements.html", context={"elements": elements, "marque": marque})

@login_required
def detail_element(request, slug):
    element = Element.objects.get(slug=slug)
    categories = Categorie.objects.exclude(slug=element.categorie.slug).all()
    marques = Marque.objects.exclude(slug=element.marque.slug).all()
    states = [(e[0], e[1]) for e in Element.STATE_CHOICES if e[0] != element.state]

    return render(request, "elements/detail_element.html",
                  context={"e": element, "categories": categories, "marques": marques, "states": states})


@login_required
def add_element(request):
    if request.POST:
        name = request.POST.get("name")
        model = request.POST.get("model")
        description = request.POST.get("description")
        price = float(request.POST.get("price"))
        count = int(request.POST.get("count"))
        caution = float(request.POST.get("caution"))
        categorie_slug = request.POST.get("categorie_slug")
        marque_slug = request.POST.get("marque_slug")
        state = request.POST.get("state")

        categorie = Categorie.objects.get(slug=categorie_slug)
        marque = Marque.objects.get(slug=marque_slug)

        elt = Element.objects.create(name=name, description=description, price=price, caution=caution, categorie=categorie, marque=marque, model=model, count=count, state=state)
        return redirect(reverse("detail_element", kwargs={"slug": elt.slug}))
    else:
        categories = Categorie.objects.all()
        marques = Marque.objects.all()
        states = Element.STATE_CHOICES

        return render(request, "elements/add_element.html",
                  context={"categories": categories, "marques": marques, "states": states})


@login_required
def delete_element(request, slug):
    element = Element.objects.get(slug=slug)
    element.delete()
    return redirect(reverse("list_elements"))


@login_required
def save_element(request, slug):
    name = request.POST.get("name")
    description = request.POST.get("description")
    model = request.POST.get("model")
    price = float(request.POST.get("price"))
    caution = float(request.POST.get("caution"))
    count = int(request.POST.get("count"))
    categorie_slug = request.POST.get("categorie_slug")
    marque_slug = request.POST.get("marque_slug")
    state = request.POST.get("state")

    categorie = Categorie.objects.get(slug=categorie_slug)
    marque = Marque.objects.get(slug=marque_slug)

    element = Element.objects.get(slug=slug)
    element.name = name
    element.model = model
    element.description = description
    element.price = price
    element.caution = caution
    element.categorie = categorie
    element.marque = marque
    element.count = count
    element.state = state
    element.save()
    return redirect(reverse('detail_element', kwargs={"slug": element.slug}))
