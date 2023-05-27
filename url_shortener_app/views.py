from django.shortcuts import render
from django.http import JsonResponse
from .models import URL
from .utilities import terminal_print_long_short_url, generate_until_unique


def home_view(request):
    return render(request, 'home.html') 


def encode(request):
    if request.method == 'POST':
        long_url = request.POST.get('url')
        if long_url:
            try:
                matching_url = URL.objects.get(long_url = long_url)
                if matching_url:
                    terminal_print_long_short_url(matching_url.long_url, matching_url.short_url)
                    return JsonResponse({"short_url": matching_url.short_url})
            except URL.DoesNotExist:
                short_url = generate_until_unique(long_url)
                return JsonResponse({"short_url":short_url})
        else:
            return JsonResponse({"error":"Please provide a URL."})
    else:
        return JsonResponse({"error": "Invalid request"})



def decode(request):
    if request.method == 'POST':
        short_url = request.POST.get('url')
        if short_url:
            database_entry = URL.objects.get(short_url = short_url)
            long_url = database_entry.long_url
            terminal_print_long_short_url(database_entry.long_url, database_entry.short_url)
            return JsonResponse({"long_url": long_url})
        else:
            return JsonResponse({"error":"Please provide a URL."})
    else:
        return JsonResponse({"error": "Invalid request"})