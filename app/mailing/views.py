from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django_project.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


@api_view(['POST'])
def car_request_view(request):
    client = request.data.get("client")
    phone_number = request.data.get("phone_number")
    car = request.data.get("car")
    send_mail('Заявка на аренду авто',
              f'Здравствуйте, меня зовут {client}, очень хотелось бы арендовать автомобиль {car}.'
              f' Перезвоните мне пожалуйста по номеру: {phone_number}.',
              DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
    return Response({"message": "OK"})

