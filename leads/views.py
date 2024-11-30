from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddLeadForm
from .models import Lead

from client.models import Client
# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by = request.user, converted=False) 

    return render(request, 'leads/leads_list.html', {
        'leads': leads
    })



@login_required
def leads_details(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead = Lead.objects.filter(created_by = request.user).get(pk=pk)

    return render(request, 'leads/leads_details.html', {
        'lead': lead
    })

@login_required
def delete_leads(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, "Leads deleted succesfully")

    return redirect('/leads_list/')

@login_required
def edit_leads(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, "Leads Edited succesfully!")

            return redirect('/leads_list/')
        
    else:

        form = AddLeadForm(instance=lead)

    return render(request, 'leads/edit_leads.html', {
        'form': form
    })



@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            messages.success(request, "Leads created succesfully")

            return redirect('/leads_list/')
        
    else:

        form = AddLeadForm()

    return render(request, 'leads/add_lead.html', {
        'form': form
    })

@login_required
def converted_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    client = Client.objects.create(
        name = lead.name,
        email = lead.email,
        description = lead.description,
        created_by = request.user
    )

    lead.converted = True
    lead.save()

    messages.success(request, "Leads converted to client succesfully")

    return redirect('/leads_list/')



