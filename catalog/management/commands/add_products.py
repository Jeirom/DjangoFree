from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test students to the database'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()

        group = Category('Смартфоны', 'Смартфоны это телефоны')
        products = [
            {'name': 'Самсунг', 'description': 'Хороший телефон', 'category': group, 'price': 11999,
             'created_at':'2025-01-19' ,'updated_at':'2025-01-19'},
            {'name': 'Самсунг1', 'description': 'Хороший телефон', 'category': group, 'price': 11999,
             'created_at': '2025-01-19', 'updated_at': '2025-01-19'},
            {'name': 'Самсунг2', 'description': 'Хороший телефон', 'category': group, 'price': 11999,
             'created_at': '2025-01-19', 'updated_at': '2025-01-19'}
        ]

        for products_data in products:
            student, created = Product.create_product(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {student.first_name} {student.last_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: {student.first_name} {student.last_name}'))