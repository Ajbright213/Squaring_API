from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class SquaringView(View):
    def get(self, request, number):
        # print(request.__dir__()) for debugging
        return HttpResponse(number ** 2)


class HelloWorldView(View):
    def get(self, request, name):
        return HttpResponse(f'Hello {name}')

class WelcomeView(View):
    def get(self, request):
        return HttpResponse('Welcome to the Squaring Page!')