from django.forms import ModelForm
from django import forms
from dartaapp.models import BookDetail, TransactionDetails, Customer, BookStore, BookImage

# Search
class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class TransactionSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class CustomerSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class BookStoreSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

# CRUD 
class BookDetailForm(ModelForm):
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BookDetail
        fields = "__all__"

class BookImageForm(ModelForm):
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BookImage
        fields = "__all__"

class TransactionDetailsForm(ModelForm):
    transaction_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = TransactionDetails
        fields = "__all__"

class CustomerForm(ModelForm):
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Customer
        fields = "__all__"

class BookStoreForm(ModelForm):
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BookStore
        fields = "__all__"