from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Airtel, Vodafone, BSNL, JIO, MTNL
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, 'Mobile/index.html')


def getdata(request):
    if request.method == 'POST':
        operator = request.POST.get('o', None)
        circle = request.POST.get('c', None)
        data = ''
        if operator == 'Airtel':
            if circle == 'ALL Circle':
                data = Airtel.objects.all()

            else:
                data = Airtel.objects.filter(circle=circle)
        elif operator == 'Vodafone':
            if circle == 'ALL Circle':
                data = Vodafone.objects.all()
            else:
                data = Vodafone.objects.filter(circle=circle)
        elif operator == 'BSNL':
            if circle == 'ALL Circle':
                data = BSNL.objects.all()
            else:
                data = BSNL.objects.filter(circle=circle)
        elif operator == 'JIO':
            if circle == 'ALL Circle':
                data = JIO.objects.all()
            else:
                data = JIO.objects.filter(circle=circle)
        elif operator == 'MTNL':
            if circle == 'ALL Circle':
                data = MTNL.objects.all()
            else:
                data = MTNL.objects.filter(circle=circle)

        ser_data = serializers.serialize('json', data)
        return JsonResponse({"valid": True, 'data': ser_data}, status=200)
    return JsonResponse({"valid": False}, status=400)
