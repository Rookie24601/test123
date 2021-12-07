from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    print("Message 1")
    return HttpResponse("Test message 123")
