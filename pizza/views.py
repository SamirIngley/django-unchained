from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.views import View  # Import the View parent class
from django.conf.urls import url
from . import views

class ShowTimeView(View):  # Create a view class

    # Change the function-based view to be called get and add the self param
    def get(self, request):
        now = datetime.now()
        html = "<html><body>Hello World! It is now {}</body></html>".format(now)
        return HttpResponse(html)
