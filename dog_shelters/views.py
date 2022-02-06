from pyexpat import model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from . import models
from django.views import generic
# TODO: Import generic views

# Create your views here.
def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class ShelterListView(generic.ListView):
    template_name = 'shelter_list.html'
    context_object_name = 'shelters'

    def get_queryset(self):
        return models.Shelter.objects.all()
            
class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

class DogUpdateView(generic.UpdateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

