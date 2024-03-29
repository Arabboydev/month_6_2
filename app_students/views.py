from django.shortcuts import render


def grands(request):
    return render(request, 'grand_about.html')


def iqtidorli_talabalar(request):
    return render(request, 'iqtidor_talabalar.html')


