from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples =[
        {'name': 'tanisha','age':23},
        {'name': 'Mickey','age':30},
        {'name': 'deek','age':24},
    ]
    for people in peoples:
       if people['age'] > 10 :
           print("yes")

    
    return render(request, "home/index.html", context={'page':'django2024','peoples':peoples})
def about(request):
    context={'page':'About'}
    return render(request,"home/about.html",context)
def contact(request):
    context={'page':'Contact'}
    return render(request,"home/contact.html",context)
def success_page(request):
    return HttpResponse("<h1>hey its success!</h1>")