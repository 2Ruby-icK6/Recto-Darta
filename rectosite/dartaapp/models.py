from django.db import models

# Create your models here.
class BaseModel (models.Model) :
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BookImage (BaseModel) :
    image_link = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) :
        return self.image_link
    
class BookDetail (BaseModel) :
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    availability = models.IntegerField(null=True, blank=True)
    book_description = models.CharField(max_length=250, null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    image = models.ForeignKey(BookImage,  blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title 
      
class BookStore (BaseModel) :
    bookstore_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)

    def __str__(self) :
        return self.bookstore_name

class Customer (BaseModel) :
    fullname = models.CharField(max_length=100, null=True, blank=True)
    book = models.ForeignKey(BookDetail, null=True, blank=True, on_delete=models.CASCADE)
    bookstore = models.ForeignKey(BookStore, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) :
        return self.fullname

class TransactionDetails (BaseModel) :
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) :
        if self.customer:
            return f"Transaction for {self.customer.fullname} on {self.transaction_date}"
        return f"Transaction without customer on {self.transaction_date}"