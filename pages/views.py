from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    message = "before default"
    message = "default message"
    req = request.__dict__
    print("Raw http request: ",req)
    print("http method: ", req['environ']['REQUEST_METHOD'])
    print("http query: ", req['environ']['QUERY_STRING'])   
    return HttpResponse("Test message 123")
