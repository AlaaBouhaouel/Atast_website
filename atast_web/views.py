from django.shortcuts import render

def index (request):
    return render(request , 'index.html')   

def index_store (request):
    return render(request , 'index_store.html')   

def ifest (request):
    return render(request , 'ifest.html')   

def maker_space (request):
    return render (request,'maker_space.html')
def xminds (request):
    return render(request,'xminds.html')

def clubs (request):
    return render(request,'clubs.html')

def test (request):
    return render(request , 'test.html')   
def genius (request):
    return render(request , 'genius.html')   

def spell (request):
    return render(request , 'spell.html')   
def ai (request):
    return render(request , 'ai.html')   

def tunibrico (request):
    return render(request , 'tunibrico.html')   
def camp (request):
    return render(request , 'camp.html')  
 
def btech (request):
    return render(request , 'btech.html')  


def training (request):
    return render(request , 'training.html')   

def cyber (request):
    return render(request , 'cyber.html')   

def oro (request):
    return render(request , 'oro.html')   
def photocontest (request):
    return render(request , 'photocontest.html')  
def team (request):
    return render(request,'team.html')
