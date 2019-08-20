from django import forms
from dashboard.models import Tour, TourPackage
from bootstrap_modal_forms.forms import BSModalForm
from django.core.exceptions import ValidationError


class TourForm(BSModalForm):
    txt_input_style = {
        'class': 'form-control text-wrap',
        'style': 'height: 100%;'
    }

    location_title = forms.CharField(widget=forms.TextInput(attrs=txt_input_style))
    description = forms.CharField(widget=forms.TextInput(attrs=txt_input_style))
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control text-wrap',
            'style': 'height: 100%;'
        }
    ))
    # tour_date_and_time = forms.DateTimeField()
    image = forms.ImageField()

    class Meta:
        model = Tour
        exclude = ('tour_date_and_time', )


class TourPackageForm(BSModalForm):
    package_title = {
        'class': 'form-control text-wrap',
        'style': 'height: 100%;'
    }
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control text-wrap',
            'style': 'height: 100%;'
        }
    ))

    # icon = forms.ImageField()

    class Meta:
        model = TourPackage
        fields = '__all__'
