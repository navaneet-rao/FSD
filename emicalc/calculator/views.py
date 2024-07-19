from django.http import JsonResponse
from django.shortcuts import render

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)  # Monthly interest rate
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return emi

def emi_calculator(request):
    if request.method == "POST":
        principal = float(request.POST.get("principal"))
        rate = float(request.POST.get("rate"))
        time = int(request.POST.get("time"))

        emi = calculate_emi(principal, rate, time)
        return JsonResponse({"emi": emi})
    return render(request, "calculator/index.html")

