from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request):
    return HttpResponse("This page was Served at " + str(datetime.now()))


def about(request):
    return HttpResponse("Hello, My name is Kartik.")
