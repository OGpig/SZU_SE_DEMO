from django.shortcuts import render

# Create your views here.
def show_contactus(request):
    return render(request,'contactus/contactus.html')