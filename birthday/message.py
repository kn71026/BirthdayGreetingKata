import datetime
from birthday.models import Birthday
from django.http import HttpResponse, JsonResponse


class BaseBirthdayMessage:
    def message(self, month=None, day=None):
        if not month or not day:
            people_list = Birthday.objects.all()
        else:
            people_list = Birthday.objects.filter(date_of_birth__month=month, date_of_birth__day=day)
        message_list = []

        for people in people_list:
            message = dict()
            message['title'] = self.get_title(people)
            message['content'] = self.get_content(people)
            message_list.append(message)

        return self.make_response(message_list)

    def get_title(self, people):
        return "Subject: Happy birthday!"

    def get_content(self, people):
        return str(people.first_name)

    def make_response(self, message_list):
        text = ""
        for message in message_list:
            text += message['title'] + "\n"
            text += message['content'] + "\n"
        return HttpResponse(text)
