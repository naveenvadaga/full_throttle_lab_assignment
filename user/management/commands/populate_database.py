from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            from user.scripts.populate_database import populate_database
            populate_database()
            self.stdout.write("populated database successfully")
        except IntegrityError:
            self.stdout.write("data base already populated with data")
