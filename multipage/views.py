from django.shortcuts import render
from . import machine_learning_model
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def result(request):

    user_input = request.GET['user_input']
    if user_input.isnumeric():
        user_input = machine_learning_model.multiplier(user_input)
        return render(request, 'result.html', {'home_input':user_input})
    else:
        return render(request, 'result.html', {'home_input':"not a number"})
