from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    time = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Hello World! this is the current server time: {time}")

def sortIntegers(request):
    numbers = [int(i) for i in request.GET["numbers"].split(",")]
    #import pdb; pdb.set_trace()
    #return HttpResponse(f"hola variable: {variable}")
    sortedList = sorted(numbers)
    data = {
        'status' : '200 ok',
        'numbers': sortedList,
        'message': "Integers sorted succesfully."
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = f"sorry {name}, eres un menor"
    else:
        message = f"Hola {name}, bienvenido a PlatziGram"
    return HttpResponse(message)
