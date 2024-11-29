from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead

# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by = request.user) 

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
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('/dashboard/')
        
    else:

        form = AddLeadForm()

    return render(request, 'leads/add_lead.html', {
        'form': form
    })
