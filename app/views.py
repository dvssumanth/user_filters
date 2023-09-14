from django.shortcuts import render

# Create your views here.
def csf(request):
    data='hi mawaa'
    d={'data':'Dsvs Sumanth'}
    return render(request,'csf.html',d)