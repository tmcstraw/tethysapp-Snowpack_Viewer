from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    return render(request, 'snowpack_viewer/home.html')

def mapview(request):
    """
    Controller for the app home page.
    """


    return render(request, 'snowpack_viewer/mapview.html')

def data_services(request):
    """
    Controller for the app home page.
    """


    return render(request, 'snowpack_viewer/data_services.html')

def about(request):
    """
    Controller for the app home page.
    """

    return render(request, 'snowpack_viewer/about.html')

def proposal(request):
    """
    Controller for the app home page.
    """

    return render(request, 'snowpack_viewer/proposal.html')
def mockup(request):
    """
    Controller for the app home page.
    """

    return render(request, 'snowpack_viewer/mockup.html')
