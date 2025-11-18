"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView

app_name = "accounts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls', namespace='accounts')),

    path('', TemplateView.as_view(template_name='accounts/login.html'), name='ui-login'),
    path('ui/register/', TemplateView.as_view(template_name='accounts/register.html'), name='ui-register'),
    path('ui/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='ui-profile'),
    path('ui/home/', TemplateView.as_view(template_name='accounts/index.html'), name='home'),
    path('ui/login/', TemplateView.as_view(template_name='accounts/login.html'), name='ui-login'),

]
