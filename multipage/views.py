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
    name = str(request.GET["name"])
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = Prediction_model.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)

    if prediction == 0:
        prediction = "You did not survive titanic voyage :("
    elif prediction == 1:
        prediction = "Yay, you survived titanic!"

    if sex == 0:
        sex = "male"
    elif sex == 1:
        sex = "female"

    if embarked == 0:
        embarked = "Southampton"
    elif embarked == 1:
        embarked = "Cherbourg"
    elif embarked == 2:
        embarked = "Queenstown"


    if title == 0:
        title = "Mr"
    elif title == 1:
        title = "Miss"
    elif title == 2:
        title = "Mrs"
    elif title == 3:
        title = "Master"
    elif title == 4:
        title = "Dr"
    elif title == 5:
        title = "Rev"
    elif title == 6:
        title = "Officer"
    elif title == 7:
        title = "Royalty"
    return render(request, 'result.html', {'prediction':prediction, 'pclass':pclass, 'sex':sex, 'age':age, 'sibsp':sibsp, 'parch':parch, 'fare':fare, 'embarked':embarked, 'title':title, 'name':name})