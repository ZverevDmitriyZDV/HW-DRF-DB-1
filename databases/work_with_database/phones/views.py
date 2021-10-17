from django.shortcuts import render
from phones.models import Phones
from django.http import HttpResponse, HttpResponseNotFound


def show_catalog(request):
    is_sorted = request.GET.get("sort")
    template = 'catalog.html'
    all_data = Phones.objects
    if is_sorted is not None:
        if is_sorted == "new":
            all_data = all_data.order_by('-release_date')
        elif is_sorted == "cheap":
            all_data = all_data.order_by('price')
        elif is_sorted == "expensive":
            all_data = all_data.order_by('-price')
        else:
            raise HttpResponseNotFound('<h1>Page not found</h1>')
    else:
       all_data = all_data.all()
    context = {'all_data': list(lin for lin in all_data)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    lin = Phones.objects.get(slug=slug)
    context = {'lin': lin}
    return render(request, template, context)
