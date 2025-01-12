

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, '../templates/catalog/home.html')


def contacts(request):
    return render(request, '../templates/catalog/contacts.html')


def post_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, number, message)
        return HttpResponse(f"Спасибо за обратную связь, {name}")
    return render(request, '../templates/catalog/contacts.html')