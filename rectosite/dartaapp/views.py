from django.shortcuts import render
from django.views.generic.list import ListView
from dartaapp.models import BookDetail, TransactionDetails, Customer, BookStore
from dartaapp.forms import BookSearchForm, TransactionSearchForm, CustomerSearchForm, BookStoreSearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class HomePageView(ListView):
    model = BookDetail
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookDetailListView(ListView):
    model = BookDetail
    content_object_name = 'bookdetails'
    template_name = "bookdetail.html"
    paginate_by = 10

    def get_queryset(self):
        return BookDetail.objects.order_by('-created_at')

class TransactionListView(ListView):
    model = TransactionDetails
    content_object_name = 'transaction'
    template_name = "transaction.html"
    paginate_by = 10

    def get_queryset(self):
        return TransactionDetails.objects.order_by('-created_at')
    
class CustomerListView(ListView):
    model = Customer
    content_object_name = 'customer'
    template_name = "customer.html"
    paginate_by = 10

    def get_queryset(self):
        return Customer.objects.order_by('-created_at')

class BookStoreListView(ListView):
    model = BookStore
    content_object_name = 'bookstore'
    template_name = "bookstore.html"
    paginate_by = 10

# Search Bar
def book_list(request):
    form = BookSearchForm(request.GET)
    query = request.GET.get('search_query')

    if query:
        books = BookDetail.objects.filter(title__icontains=query)
    else:
        books = BookDetail.objects.all()

    # books = books.order_by('title') 
    paginator = Paginator(books, 10)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:

        books = paginator.page(paginator.num_pages)
        
    context = {
        'object_list': books,
        'form': form,
    }
    
    return render(request, 'search/searchbook.html', context)

def transaction_list(request):
    form = TransactionSearchForm(request.GET)
    query = request.GET.get('search_query')

    if query:
        transaction = TransactionDetails.objects.filter(customer__fullname__icontains=query)
    else:
        transaction = TransactionDetails.objects.all()
    
    paginator = Paginator(transaction, 10)
    page = request.GET.get('page')

    try:
        transaction = paginator.page(page)
    except PageNotAnInteger:
        transaction = paginator.page(1)
    except EmptyPage:

        transaction = paginator.page(paginator.num_pages)

    context = {
        'object_list': transaction,
        'form': form,
    }
    return render(request, 'search/searchtransaction.html', context)

def customer_list(request):
    form = CustomerSearchForm(request.GET)
    query = request.GET.get('search_query')

    if query:
        customer = Customer.objects.filter(fullname__icontains=query)
    else:
        customer = Customer.objects.all()
    
    paginator = Paginator(customer, 10)
    page = request.GET.get('page')

    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:

        customer = paginator.page(paginator.num_pages)

    context = {
        'object_list': customer,
        'form': form,
    }
    return render(request, 'search/searchcustomer.html', context)

def bookstore_list(request):
    form = BookStoreSearchForm(request.GET)
    query = request.GET.get('search_query')

    if query:
        bookstore = BookStore.objects.filter(bookstore_name__icontains=query)
    else:
        bookstore = BookStore.objects.all()
    
    paginator = Paginator(bookstore, 10)
    page = request.GET.get('page')

    try:
        bookstore = paginator.page(page)
    except PageNotAnInteger:
        bookstore = paginator.page(1)
    except EmptyPage:
        bookstore = paginator.page(paginator.num_pages)

    context = {
        'object_list': bookstore,
        'form': form,
    }
    return render(request, 'search/searchbookstore.html', context)