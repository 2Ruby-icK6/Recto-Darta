from django.contrib import admin
from django.urls import path
from dartaapp.views import HomePageView, BookDetailListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('bookdetails_list/', BookDetailListView.as_view(), name='bookdetails-list'),
]
