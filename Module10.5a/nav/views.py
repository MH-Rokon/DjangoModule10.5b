from django.shortcuts import render
def  home(request):
    return render(request,'nav/home.html')
def  contact(request):
    return render(request,'nav/contact.html')



 
