from tkinter import N
from django.shortcuts import render
from matplotlib.style import context
from . import Prediction_model

def home(request):
    
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def Cardata(request):
    return render(request, 'Cardata.html')

def Cardata1(request):
    return render(request, 'Cardata1.html')
    
def titanic(request):
    return render(request,'titanic.html')

def result(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = Prediction_model.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request, 'result.html', {'prediction':prediction})