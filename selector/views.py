from rest_framework.response import Response
from rest_framework import viewsets
from .models import CarType, Model, Make



class UserInputText(viewsets.ViewSet):
    def input_text(self, request):
        text = request.query_params.get("text")
        texts_to_search = text.split()

        makes = Make.objects.all()
        models = Model.objects.all()
        car_types = CarType.objects.all()

        filtered_makes = Make.objects.none()
        filtered_models = Model.objects.none()
        filtered_car_types = CarType.objects.none()

        for word in texts_to_search:
            if word:
                makes_filtered = makes.filter(name__icontains=word)
                filtered_makes = filtered_makes.union(makes_filtered)

                models_filtered = models.filter(name__icontains=word)
                filtered_models = filtered_models.union(models_filtered)

                car_types_filtered = car_types.filter(name__icontains=word)
                filtered_car_types = filtered_car_types.union(car_types_filtered)

        year = texts_to_search[-1]
        # print(year)


        final_filtered_car_types = self.search_with_years(year, filtered_car_types)

        filtered_car_types = filtered_car_types.union(final_filtered_car_types)

        results = []
        if filtered_car_types.exists():
            for car in filtered_car_types:
                result = {
                    "make": car.model.make.name,
                    "model": car.model.name,
                    "car_type": car.name,
                    "car_type_id": car.id
                }
                results.append(result)
            return Response({"items": results})
        else:
            return Response({"items": []})

    def search_with_years(self, year, car_types):
        year = int(year)

        filtered_car_types = CarType.objects.none()

        for car_type in car_types:
            car_year_string = car_type.name
            parts = car_year_string.split('(')



            year_range_1 = parts[-1].strip(' )')
            year_range = year_range_1.strip()

            if year_range.endswith('-'):
                year_range = year_range.rstrip('-').strip()


            year_range_parts = year_range.split('-')
            # print(year_range_parts) 2012 2015

            # წელში თუ წერია 2022, 2022-2024 ჩათვალეთ

            # არ გამომივიდა

            start_year = int(year_range_parts[0].strip())
            if len(year_range_parts) > 1:
                end_year = int(year_range_parts[1].strip())
            else:
                end_year = start_year


            if start_year <= year <= end_year:
                filtered_car_types = filtered_car_types.union(CarType.objects.filter(id=car_type.id))

        return filtered_car_types