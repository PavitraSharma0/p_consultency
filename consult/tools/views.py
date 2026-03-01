import requests
from django.shortcuts import render

def tools_dashboard(request):

    currency_data = {}
    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        if r.status_code == 200:
            currency_data = r.json()
    except:
        currency_data = {"error": "Currency API not working"}

    return render(request, "consultancy_tools.html", {
        "currency": currency_data,
    })