"""
URL configuration for CryptoPlus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import IndexPage
from .views import Yield
from .views import Contacto
from .views import PricesHistoric


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(),name="index"),
    path("index.html/", IndexPage.as_view(),name="index"),
    path("yield.html/", Yield.as_view(),name="yield"),
    path("contacto.html/", Contacto.as_view(),name="contacto"),
    path("pricesHistoric.html/", PricesHistoric.as_view(),name="pricesHistoric"),
]