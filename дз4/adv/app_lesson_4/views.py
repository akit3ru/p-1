from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advert
from .forms import AdvertForm


def index(request):
    advertisements = Advert.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advert(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
