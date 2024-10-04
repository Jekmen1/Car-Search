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

            year_info = type_row.split('(')
            if len(year_info) > 1:
                year_range_string = year_info[-1].strip(' )')
                year_range_parts = year_range_string.split('-')

                start_year = int(year_range_parts[0].strip())

                if len(year_range_parts) > 1 and year_range_parts[1].strip():
                    end_year = int(year_range_parts[1].strip())
                else:
                    end_year = start_year + 2
            else:
                continue

            make = Make.objects.get_or_create(name=make_row)[0]
            model = Model.objects.get_or_create(name=model_row, make=make)[0]

            car_type = CarType.objects.get_or_create(
                name=type_row,
                model=model,
                defaults={'release_start_year': start_year, 'release_end_year': end_year}
            )[0]

            car_type.start_year = start_year
            car_type.end_year = end_year
            car_type.save()
