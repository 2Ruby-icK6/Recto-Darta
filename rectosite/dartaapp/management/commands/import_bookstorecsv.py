import csv
from django.core.management.base import BaseCommand
from dartaapp.models import BookStore

class Command(BaseCommand):
    help = 'Import data from a CSV file into Book model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r', encoding='utf-8', errors='replace') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    BookStore.objects.create(
                        bookstore_name=row['bookstore_name'],
                        address=row['address'],
                        postal_code=row['postal_code']
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {str(e)}'))
