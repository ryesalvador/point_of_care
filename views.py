from django.shortcuts import render
from point_of_care.models import Resident

# Create your views here.
def index(request):
    num_residents = Resident.objects.all().count()
    context = {
        'num_residents': num_residents,    
    }
    return render(request, 'point_of_care/index.html', context=context)
