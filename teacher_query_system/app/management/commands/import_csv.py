import csv
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from app.models import Teacher

class Command(BaseCommand):
    help = "import csv data into database"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv_file', help='Path to the CSV file')
    
    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Teacher.objects.create(
                    department = row['Department'],
                    name = row['Name'],
                    title = row['Title'],
                    photo = row['Photo']
                )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
