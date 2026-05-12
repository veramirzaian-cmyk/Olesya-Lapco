from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing/index.html', {
        "telegram_link": "https://t.me/LapkOlesya"
    })
