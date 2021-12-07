from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    message = "before default"
    message = "default message"
    print(request.GET)
    return HttpResponse("Test message 123")
