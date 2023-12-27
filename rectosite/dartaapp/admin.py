from django.contrib import admin
from .models import  BookDetail, BookImage, BookStore, Customer, TransactionDetails

# Register your models here.
# Display all fields from models including created_at and updated_at
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

class BookDetailAdmin(BaseModelAdmin):
    list_display = ('title', 'category', 'price', 'availability', 'book_description', 'stars', 'image_id', 'created_at', 'updated_at')
    
class BookImageAdmin(BaseModelAdmin):
    list_display = ('image_link', 'created_at', 'updated_at')

class BookStoreAdmin(BaseModelAdmin):
    list_display = ('bookstore_name', 'address', 'postal_code', 'created_at', 'updated_at')

class CustomerAdmin(BaseModelAdmin):
    list_display = ('fullname', 'book_id', 'bookstore_id', 'created_at', 'updated_at')

class TransactionDetailsAdmin(BaseModelAdmin):
    list_display = ('customer_id', 'payment_method', 'transaction_date', 'created_at', 'updated_at')

# Register your models here.
# admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail, BookDetailAdmin)
admin.site.register(BookImage, BookImageAdmin)
admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(TransactionDetails, TransactionDetailsAdmin)