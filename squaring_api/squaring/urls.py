# from django.contrib import admin
from django.urls import path

from squaring.views import SquaringView, HelloWorldView, WelcomeView
# sqauring.view.SquaringView
urlpatterns = [
    path('<int:number>/', SquaringView.as_view()),
    path('hello/<name>', HelloWorldView.as_view()),
    path('', WelcomeView.as_view())
]