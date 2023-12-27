import csv
from django.core.management.base import BaseCommand
from dartaapp.models import Customer, BookDetail, BookStore

class Command(BaseCommand):
    help = 'Import data from a CSV file into Customer model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r', encoding='utf-8', errors='replace') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    book_id = row['book_id']
                    bookstore_id = row['bookstore_id']

                    # Retrieve Book and Bookstore instances based on the IDs
                    book = BookDetail.objects.get(pk=book_id)
                    bookstore = BookStore.objects.get(pk=bookstore_id)

                    Customer.objects.create(
                        fullname=row['fullname'],
                        book=book,
                        bookstore=bookstore
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {str(e)}'))
