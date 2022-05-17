# import requests_unixsocket.testutils
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
# Create your views here.
from employer.forms import EmployerProfileForm
from employer.models import EmployerProfile


class EmployerHome(TemplateView):
    template_name = "employer_home.html"


class EmployerFormCreateView(CreateView):
    form_class = EmployerProfileForm
    template_name = "employer_profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = EmployerProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.user = request.user
    #         profile.save()
    #         return render(request,"employer_home.html")
    #     else:
    #         return render(request,{self.form_class},"employer_profile.html")

