from django.shortcuts import render
from point_of_care.models import Resident, Intervention
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
@login_required
def index(request):
    num_residents = Resident.objects.all().count()
    context = {
        'num_residents': num_residents,    
    }
    return render(request, 'point_of_care/index.html', context=context)

class ResidentListView(LoginRequiredMixin, generic.ListView):
    model = Resident
    paginate_by = 10

class ResidentDetailView( LoginRequiredMixin, generic.DetailView):
    model = Resident

class ResidentCreate(LoginRequiredMixin, generic.CreateView):
    model = Resident
    fields = '__all__'

class ResidentUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Resident
    fields = '__all__'
    template_name_suffix = '_update_form'

class ResidentDelete(LoginRequiredMixin, generic.DeleteView):
    model = Resident
    success_url = reverse_lazy('residents')

class InterventionListView(LoginRequiredMixin, generic.ListView):
    model = Intervention
    paginate_by = 10

class InterventionDetailView( LoginRequiredMixin, generic.DetailView):
    model = Intervention
