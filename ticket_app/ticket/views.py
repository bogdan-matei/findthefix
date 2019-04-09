from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Model
from .mail_service import email_confirmation


def home(request):
    form = TicketForm()
    response = render(request, 'purchase/home.html', {'form': form})
    response['Env_VM'] = 'Team6'
    return response


def purchase(request):
    if request.method == "POST":
        ticket = Model()
        form = TicketForm(instance=ticket, data=request.POST)
        if form.is_valid():
            form.save()
            email_confirmation(request)
            return redirect('successful_acquisition')
        response = render(request, 'purchase/failed_acquisition.html')
    else:
        form = TicketForm()
        response = render(request, 'purchase/home.html', {'form': form})
    response['Env_VM'] = 'Team6'
    return response


def successful_acquisition(request):
    response = render(request, 'purchase/successful_acquisition.html')
    response['Env_VM'] = 'Team6'
    return response
