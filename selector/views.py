from rest_framework import viewsets
from rest_framework.response import Response
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

        year = None

        if texts_to_search[-1].isdigit():
            year = int(texts_to_search.pop())

        for word in texts_to_search:
            if word:

                makes_filtered = makes.filter(name__icontains=word)
                filtered_makes = filtered_makes.union(makes_filtered)

                models_filtered = models.filter(name__icontains=word)
                filtered_models = filtered_models.union(models_filtered)

                car_types_filtered = car_types.filter(name__icontains=word)
                filtered_car_types = filtered_car_types.union(car_types_filtered)


        if year:
            filtered_car_types = car_types.filter(release_start_year__lte=year, release_end_year__gte=year).union(filtered_car_types)


        results = []
        if filtered_car_types.exists():
            for car in filtered_car_types:
                result = {
                    "make": car.model.make.name,
                    "model": car.model.name,
                    "car_type": car.name,
                    "car_type_id": car.id,
                }
                results.append(result)

        return Response({"items": results})
