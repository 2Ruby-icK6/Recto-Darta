import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from dartaapp.models import TransactionDetails, Customer

class Command(BaseCommand):
    help = 'Import data from a CSV file into TransactionDetails model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r', encoding='utf-8', errors='replace') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    # Retrieve the Customer instance based on the provided customer_id
                    customer_id = row['customer_id']
                    customer = Customer.objects.get(id=customer_id)

                    transaction_date_str = row['transaction_date']
                    transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d %H:%M:%S")
                    aware_transaction_date = make_aware(transaction_date)

                    TransactionDetails.objects.create(
                        customer=customer,
                        payment_method=row['payment_method'],
                        transaction_date=aware_transaction_date
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {str(e)}'))
