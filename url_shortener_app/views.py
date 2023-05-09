from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import URL
from .utilities import generate_url


def home_view(request):
    return render(request, 'home.html') 


@csrf_exempt
def encode(request):
    if request.method == 'POST':
        long_url = request.POST.get('url')
        # Check if the long URL already exists in the database
        if long_url:
            try:
                match = URL.objects.get(long_url = long_url)
                if match:
                    # If it exists, return the corresponding short URL
                    return JsonResponse({"short_url": match.short_url})
            except URL.DoesNotExist:
                # If it does not exist, generate a new short URL
                while True:
                    short_url = generate_url()
                    try: 
                        URL.objects.get(short_url = short_url)
                    except URL.DoesNotExist:
                        # Save the new URL entry to the database
                        new_url = URL(long_url = long_url, short_url = short_url)
                        new_url.save()
                        break
                # Return the new short URL
                return JsonResponse({"short_url":short_url})
        else:
            # If the URL is not provided in the POST request, return an error message
            return JsonResponse({"error":"Please provide a URL."})
    else:
        # If the request method is not POST, return an error message
        return JsonResponse({"error": "Invalid request"})


@csrf_exempt
def decode(request):
    if request.method == 'POST':
        short_url = request.POST.get('url')
        if short_url:
            # Find the corresponding database entry for the short URL
            database_entry = URL.objects.get(short_url = short_url)
            long_url = database_entry.long_url
            # Return the long URL
            return JsonResponse({"long_url": long_url})
        else:
            # If the URL is not provided in the POST request, return an error message
            return JsonResponse({"error":"Please provide a URL."})
    else:
        # If the request method is not POST, return an error message
        return JsonResponse({"error": "Invalid request"})