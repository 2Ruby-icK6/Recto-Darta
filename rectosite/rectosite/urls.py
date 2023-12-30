from django.contrib import admin
from django.urls import path
from dartaapp.views import HomePageView, BookDetailListView, TransactionListView, CustomerListView, BookStoreListView
from dartaapp.views import book_list, transaction_list, customer_list, bookstore_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('bookdetails_list/', BookDetailListView.as_view(), name='bookdetails-list'),
    path('transaction_list/', TransactionListView.as_view(), name='transaction-list'),
    path('bookstore_list/', BookStoreListView.as_view(), name='bookstore-list'),
    path('customer_list/', CustomerListView.as_view(), name='customer-list'),
    path('books/', book_list, name='book-search'),
    path('transaction/', transaction_list, name='transaction-search'),
    path('customer/', customer_list, name='customer-search'),
    path('bookstore/', bookstore_list, name='bookstore-search'),
]
