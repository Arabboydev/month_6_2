from django.shortcuts import render


def book_list(request):
    return render(request, 'book_l.html')


def users_list(request):
    return render(request, 'users_l.html')
