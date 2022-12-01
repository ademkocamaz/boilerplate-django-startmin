from django.shortcuts import render

def root(request):
    return render(request, 'root.html')
def index(request):
    return render(request, 'pages/index.html')
def charts_flot(request):
    return render(request, 'pages/flot.html')
def charts_morris(request):
    return render(request, 'pages/morris.html')