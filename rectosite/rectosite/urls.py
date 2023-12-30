from django.contrib import admin
from django.urls import path
from dartaapp.views import HomePageView, BookDetailListView, TransactionListView, CustomerListView, BookStoreListView, BookImageListView
from dartaapp.views import book_list, transaction_list, customer_list, bookstore_list
from dartaapp.views import BookDetailCreateView, BookDetailDeleteView, BookDetailUpdateView
from dartaapp.views import TransactionDetailsCreateView, TransactionDetailsDeleteView, TransactionDetailsUpdateView
from dartaapp.views import CustomerCreateView, CustomerDeleteView, CustomerUpdateView
from dartaapp.views import BookStoreCreateView, BookStoreDeleteView, BookStoreUpdateView
from dartaapp.views import BookImageCreateView, BookImageDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('bookdetails_list/', BookDetailListView.as_view(), name='bookdetails-list'),
    path('transaction_list/', TransactionListView.as_view(), name='transaction-list'),
    path('bookstore_list/', BookStoreListView.as_view(), name='bookstore-list'),
    path('customer_list/', CustomerListView.as_view(), name='customer-list'),
    path('bookimage_list/', BookImageListView.as_view(), name='bookimage-list'),
    path('books/', book_list, name='book-search'),
    path('transaction/', transaction_list, name='transaction-search'),
    path('customer/', customer_list, name='customer-search'),
    path('bookstore/', bookstore_list, name='bookstore-search'),

    path('bookdetails_list/add', BookDetailCreateView.as_view(), name='bookdetails-add'),
    path('bookdetails_list/<pk>',  BookDetailUpdateView.as_view(), name='bookdetails-update'),
    path('bookdetails_list/<pk>/delete',  BookDetailDeleteView.as_view(), name='bookdetails-delete'),

    path('transaction_list/add', TransactionDetailsCreateView.as_view(), name='transaction-add'),
    path('transaction_list/<pk>',  TransactionDetailsUpdateView.as_view(), name='transaction-update'),
    path('transaction_list/<pk>/delete',  TransactionDetailsDeleteView.as_view(), name='transaction-delete'),

    path('customer_list/add', CustomerCreateView.as_view(), name='customer-add'),
    path('customer_list/<pk>',  CustomerUpdateView.as_view(), name='customer-update'),
    path('customer_list/<pk>/delete',  CustomerDeleteView.as_view(), name='customer-delete'),

    path('bookstore_list/add', BookStoreCreateView.as_view(), name='bookstore-add'),
    path('bookstore_list/<pk>',  BookStoreUpdateView.as_view(), name='bookstore-update'),
    path('bookstore_list/<pk>/delete',  BookStoreDeleteView.as_view(), name='bookstore-delete'),

    path('bookimage_list/add', BookImageCreateView.as_view(), name='bookimage-add'),
    path('bookimage_list/<pk>/delete',  BookImageDeleteView.as_view(), name='bookimage-delete'),
]
