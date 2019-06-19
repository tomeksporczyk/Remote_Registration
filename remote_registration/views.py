from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from remote_registration.forms import *


class HomeView(View):
    def get(self, request):
        return render(request, 'remote_registration/base.html')


class AddMedicalInstitution(FormView):
    form_class = AddMedicalInstitutionForm
    template_name = "remote_registration/uni_form_add.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data.get('name').upper()
        city = form.cleaned_data.get('city').upper()
        address = form.cleaned_data.get('address').upper()
        ward = form.cleaned_data.get('ward').upper()
        institution = MedicalInstitution.objects.filter(name=name,
                                                        city=city,
                                                        address=address,
                                                        ward=ward)
        print(institution.count())
        if institution.count() == 0:
            form.save()
            return super().form_valid(form)
        self.success_url = reverse_lazy('add_institution')
        return super().form_valid(form)


class AddProcedure(FormView):
    form_class = AddProcedureForm
    template_name = 'remote_registration/uni_form_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data.get('name').upper()
        details = form.cleaned_data.get('details').upper()
        duration = form.cleaned_data.get('duration')
        procedure = Procedure.objects.filter(name=name,
                                             details=details,
                                             duration=duration,
                                             )
        if procedure.count() == 0:
            form.save()
            return super().form_valid(form)
        self.success_url = reverse_lazy('add_procedure')
        return super().form_valid(form)


class AddPersonnel(FormView):
    form_class = AddPersonnelForm
    template_name = 'remote_registration/uni_form_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data.get('name').upper()
        surname = form.cleaned_data.get('surname').upper()
        personnel = Personnel.objects.filter(name=name,
                                             surname=surname)
        if personnel.count() == 0:
            form.save()
            return super().form_valid(form)
        self.success_url = reverse_lazy('add_personnel')
        return super().form_valid(form)

