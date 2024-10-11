from django.urls import path
from .import views as v
from .views import *

urlpatterns =[
    path("",IndexView.as_view(),name="index"),
    path("about",AboutView.as_view(),name="about"),
    path("services",ServiceView.as_view(),name="services"),
    path("blogs",BlogsView.as_view(),name="blogs"),
    path("contact",ContactView.as_view(),name="contact")
]
