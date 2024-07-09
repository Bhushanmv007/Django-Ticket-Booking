from django.shortcuts import render
from django.http import JsonResponse
import math

def emi_calculator(principal, rate, time):
    rate = rate / (12 * 100)  # Monthly interest rate
    time = time * 12  # Number of months
    emi = (principal * rate * math.pow(1 + rate, time)) / (math.pow(1 + rate, time) - 1)
    return emi

def calculate_emi(request):
    if request.method == 'GET':
        principal = float(request.GET.get('principal'))
        rate = float(request.GET.get('rate'))
        time = float(request.GET.get('time'))
        emi = emi_calculator(principal, rate, time)
        return JsonResponse({'emi': round(emi, 2)})

def index(request):
    return render(request, 'calculator/index.html')
