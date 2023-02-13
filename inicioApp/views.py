from django.shortcuts import render

# Create your views here.
def inicioDef(request):
    return render(request,'inicio.html',{})
def paginaDef(request):
    return render(request,'pagina.html',{})
