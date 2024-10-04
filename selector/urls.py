from django.urls import path
from .views import UserInputText

urlpatterns = [
    path('search/', UserInputText.as_view({"get": "input_text"})),
]

