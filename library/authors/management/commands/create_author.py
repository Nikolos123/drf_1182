from django.core.management.base import BaseCommand

from authors.models import Authors


class Command(BaseCommand):
    def handle(self, *args, **options):

        Authors.objects.create(first_name='test',last_name='test',birthday_year=1111)