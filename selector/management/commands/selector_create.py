from django.core.management.base import BaseCommand
import pandas as pd
from ...models import Model, Make, CarType

class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_excel('cars.xlsx')

        for index, row in df.iterrows():
            make_row = row['Make']
            model_row = row['Model']
            type_row = row['Type']

            make, created = Make.objects.get_or_create(name=make_row)
            if created:
                make.save()

            model, created = Model.objects.get_or_create(name=model_row, make=make)
            if created:
                model.save()

            car_type, created = CarType.objects.get_or_create(name=type_row, model=model)
            if created:
                car_type.save()

