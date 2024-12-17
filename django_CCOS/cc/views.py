from django.shortcuts import render

# Create your views here.
def show_competitione(request):
    return render(request, 'cc/cc.html')
