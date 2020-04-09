from django.shortcuts import render
from point_of_care.models import Resident
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
