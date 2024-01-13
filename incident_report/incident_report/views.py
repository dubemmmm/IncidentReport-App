from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout
from incident_app.models import Incident
from django.contrib import messages

class LandingView(generic.TemplateView):
    template_name = 'landing.html'
    
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
  
    
class ThanksView(generic.TemplateView):
    template_name = 'thanks.html'
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request) 
        return render(request, self.template_name)