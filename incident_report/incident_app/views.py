import json
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import IncidentForm
from .models import Incident
from django.urls import reverse_lazy
import requests
from django.contrib import messages
# Create your views here.
class CreateIncident(LoginRequiredMixin, generic.CreateView):
    form_class = IncidentForm
    template_name = 'incident_app/incident_form.html'
    model = Incident
    success_url = reverse_lazy('reports:all')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/' + ip_data['ip'])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        form.instance.address = location_data['city']
        form.instance.latitude = location_data['lat']
        form.instance.longitude = location_data['lon']
        form.instance.country = location_data['country']
        

        return super().form_valid(form)
    
    
class IncidentList(LoginRequiredMixin, generic.ListView):
    template_name = 'incident_app/incident_list.html'
    model = Incident
    context_object_name = 'incident_list'
    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Incident.objects.filter(category=category).order_by('-timestamp')
        else:
            return Incident.objects.all().order_by('-timestamp')
        
class IncidentListUser(LoginRequiredMixin, generic.ListView):
    template_name = 'incident_app/incident_list_user.html'
    model = Incident
    context_object_name = 'incident_list_user'
    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user).order_by('-timestamp')
    
class IncidentDetails(LoginRequiredMixin, generic.DetailView):
    template_name = 'incident_app/incident_details.html'
    model = Incident
    context_object_name = 'incidents'

    