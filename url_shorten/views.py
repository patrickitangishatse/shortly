from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Url
import string
import random

def home(request):
    all_urls = Url.objects.all()
    return render(request, 'index.html', {'all_urls': all_urls})

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = generate_short_url()
        url_instance = Url.objects.create(long_url=long_url, short_url=short_url)
        return redirect('home')
    return redirect('home')
def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not Url.objects.filter(short_url=short_url).exists():
            return short_url
def redirect_to_long_url(request, short_url):
    url_instance = get_object_or_404(Url, short_url=short_url)
    return redirect(url_instance.long_url)