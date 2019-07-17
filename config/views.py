from django.shortcuts import render, HttpResponseRedirect


# Create your views here.


def links(request):
    return HttpResponseRedirect('links')
