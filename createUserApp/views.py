from django.shortcuts import render

# Create your views here.

def createUserPage(request):
    return render(request, 'createUserApp/index.html')
