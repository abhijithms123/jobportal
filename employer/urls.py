from django.urls import path
from employer import views
urlpatterns=[
    path("ehome",views.EmployerHome.as_view(),name="emp-home"),
    path("eprofile",views.EmployerFormCreateView.as_view(),name="emp-profile"),
]