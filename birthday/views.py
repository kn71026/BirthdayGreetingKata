from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, ListAPIView
import datetime
from birthday.models import Birthday
from birthday.serializers import BirthdaySerializer
from birthday.message import *


class BirthdayByDate(ListAPIView):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer

    def get(self, request, *args, **krgs):
        # 根據不同version呼叫不同class
        birthday_message = BirthdayMessageV1()
        date = self.request.GET.get('date', None)
        if date is not None:
            try:
                date = datetime.datetime.strptime(date, "%m%d")
                message_data = birthday_message.get(date.month, date.day)
            except Exception as e:
                message_data = {'error': str(e)}
        else:
            message_data = birthday_message.get()
        return message_data
