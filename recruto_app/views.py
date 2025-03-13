from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
   
    if not name or not message:
        return HttpResponse("Выполните GET-запрос с параметрами name и message.")

    return HttpResponse(f"Hello {name}! {message}")
