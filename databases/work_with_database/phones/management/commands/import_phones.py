import csv

from django.core.management.base import BaseCommand
from phones.models import Phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for dt_l in phone_reader:
                new_line = Phones.objects.create(id=int(dt_l[0]),
                                                 name=dt_l[1],
                                                 price=int(dt_l[3]),
                                                 image=dt_l[2],
                                                 release_date=dt_l[4],
                                                 lte_exists=dt_l[5])
                new_line.save()
