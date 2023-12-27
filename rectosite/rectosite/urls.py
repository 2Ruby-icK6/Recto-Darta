from django.contrib import admin
from django.urls import path
from dartaapp.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
]
