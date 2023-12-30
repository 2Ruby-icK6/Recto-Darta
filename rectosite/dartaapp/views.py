from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dartaapp.models import BookDetail, TransactionDetails, Customer, BookStore, BookImage
from dartaapp.forms import BookSearchForm, TransactionSearchForm, CustomerSearchForm, BookStoreSearchForm
from dartaapp.forms import BookDetailForm, TransactionDetailsForm, CustomerForm, BookStoreForm, BookImageForm


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

    def get_queryset(self):
        return BookStore.objects.order_by('-created_at')

class BookImageListView(ListView):
    model = BookImage
    content_object_name = 'bookimage'
    template_name = "bookimage.html"
    paginate_by = 10

    def get_queryset(self):
        return BookImage.objects.all().order_by('created_at') 
    
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

# ==================================================================
# ==================================================================
# ==================================================================

class BookDetailCreateView(CreateView):
    model = BookDetail
    form_class = BookDetailForm
    template_name = 'CRUD/bookcrud/add.html'
    success_url = reverse_lazy('bookdetails-list')

class BookDetailUpdateView(UpdateView):
    model = BookDetail
    form_class = BookDetailForm
    template_name = 'CRUD/bookcrud/update.html'
    success_url = reverse_lazy('bookdetails-list')

class BookDetailDeleteView(DeleteView):
    model = BookDetail
    template_name = 'CRUD/bookcrud/delete.html'
    success_url = reverse_lazy('bookdetails-list')

# ==================================================================
# ==================================================================
# ==================================================================
    
class TransactionDetailsCreateView(CreateView):
    model = TransactionDetails
    form_class = TransactionDetailsForm
    template_name = 'CRUD/transactioncrud/add.html'
    success_url = reverse_lazy('transaction-list')

class TransactionDetailsUpdateView(UpdateView):
    model = TransactionDetails
    form_class = TransactionDetailsForm
    template_name = 'CRUD/transactioncrud/update.html'
    success_url = reverse_lazy('transaction-list')

class TransactionDetailsDeleteView(DeleteView):
    model = TransactionDetails
    template_name = 'CRUD/transactioncrud/delete.html'
    success_url = reverse_lazy('transaction-list')

# ==================================================================
# ==================================================================
# ==================================================================
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'CRUD/customercrud/add.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'CRUD/customercrud/update.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'CRUD/customercrud/delete.html'
    success_url = reverse_lazy('customer-list')

# ==================================================================
# ==================================================================
# ==================================================================
    
class BookStoreCreateView(CreateView):
    model = BookStore
    form_class = BookStoreForm
    template_name = 'CRUD/bookstorecrud/add.html'
    success_url = reverse_lazy('bookstore-list')

class BookStoreUpdateView(UpdateView):
    model = BookStore
    form_class = BookStoreForm
    template_name = 'CRUD/bookstorecrud/update.html'
    success_url = reverse_lazy('bookstore-list')

class BookStoreDeleteView(DeleteView):
    model = BookStore
    template_name = 'CRUD/bookstorecrud/delete.html'
    success_url = reverse_lazy('bookstore-list')

# ==================================================================
# ==================================================================
# ==================================================================
    
class BookImageCreateView(CreateView):
    model = BookImage
    form_class = BookImageForm
    template_name = 'CRUD/bookimagecrud/add.html'
    success_url = reverse_lazy('bookimage-list')

class BookImageDeleteView(DeleteView):
    model = BookImage
    template_name = 'CRUD/bookimagecrud/delete.html'
    success_url = reverse_lazy('bookimage-list')