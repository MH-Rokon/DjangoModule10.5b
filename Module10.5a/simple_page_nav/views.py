from django.shortcuts import render
def  home(request):
    return render(request,'nav/home.html')
def  index(request):
    return render(request,'index.html')

 
