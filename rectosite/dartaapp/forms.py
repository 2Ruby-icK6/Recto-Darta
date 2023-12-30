from django import forms

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class TransactionSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class CustomerSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')

class BookStoreSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')