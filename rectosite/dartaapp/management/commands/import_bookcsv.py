import csv
from django.core.management.base import BaseCommand
from dartaapp.models import BookDetail, BookImage

class Command(BaseCommand):
    help = 'Import data from a CSV file into BookDetail model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r', encoding='utf-8', errors='replace') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    # Assuming image_id is a foreign key to Image model
                    image_id = row['image_id']
                    image = BookImage.objects.get(pk=image_id)

                    BookDetail.objects.create(
                        title=row['title'],
                        category=row['category'],
                        price=row['price'],
                        availability=row['availability'],
                        book_description=row['book_description'],
                        image=image,  # Assign the related instance
                        stars=row['stars']
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {str(e)}'))
