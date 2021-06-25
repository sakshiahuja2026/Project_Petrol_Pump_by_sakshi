"""Project_Petrol_Pump URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user.views import home
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home-page"),
    path("",LoginView.as_view(template_name='user/login.html'),name="login"),
    path("logout",LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path("rates/",include("rates.urls")),
    path("nozzel/",include("nozzel.urls")),
    path("employee/",include("employee.urls")),
    path("tank/",include("tank.urls")),
    path("creditor/",include("creditor.urls"))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
