from django.shortcuts import render

# Create your views here.
def show_competition(request):
    return render(request, 'home_page/home_page.html')