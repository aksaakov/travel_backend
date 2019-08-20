from .models import Tour, TourPackage
from . import models as md
from django.shortcuts import redirect, render
from dashboard.forms import TourForm, TourPackageForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalDeleteView, BSModalUpdateView, BSModalCreateView
from rest_framework import viewsets
from dashboard.serializers import TourSerializer


# Create your views here.
def index(request):
    tours = Tour.objects.all()

    context = {
        'title': 'Tours',
        'tours': tours
    }

    if request.user.is_authenticated:
        return render(request, 'tours/index.html', context)
    else:
        return redirect('accounts/login/') 


class TourCreate(BSModalCreateView):
    form_class = TourForm
    success_message = 'Success: Tour was created.'
    template_name = 'tours/tourModals/create_tour.html'
    success_url = reverse_lazy('index')
    

class TourUpdate(BSModalUpdateView):
    model = Tour
    form_class = TourForm
    template_name = 'tours/tour.html'
    success_url = reverse_lazy('index')


class TourDelete(BSModalDeleteView):
    model = md.Tour
    success_message = 'Success: Tour was deleted.'
    template_name = 'tours/tourModals/delete_tour.html'
    success_url = reverse_lazy('index')
    

class ToursViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tours to be viewed.
    """
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    http_method_names = ['get']
    
    
def packages(request):
    tour_packages = TourPackage.objects.all()

    context = {
        'title': 'Packages',
        'pkgs': tour_packages
    }

    if request.user.is_authenticated:
        return render(request, 'tourPackages/all_packages.html', context)
    else:
        return redirect('accounts/login/') 


class PackageUpdate(BSModalUpdateView):
    model = md.TourPackage
    form_class = TourPackageForm
    success_message = 'Success: Tour Package was updated.'
    template_name = 'tourPackages/packageModals/update_package.html'
    success_url = reverse_lazy('tour_packages')
