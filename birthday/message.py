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


class BirthdayMessageV1(BaseBirthdayMessage):
    def get_content(self, people):
        return "Happy birthday, dear " + str(people.first_name) + "!"


class BirthdayMessageV2(BaseBirthdayMessage):
    def get_content(self, people):
        if people.gender == 'Male':
            return "Happy birthday, dear " + str(
                people.first_name) + "!\nWe offer special discount 20% off for the following items:" \
                                     "\nWhiteWine, iPhoneX"
        elif people.gender == 'Female':
            return "Happy birthday, dear " + str(
                people.first_name) + "!\nWe offer special discount 50% off for the following items:" \
                                     "\nCosmetic, LV Handbags"


class BirthdayMessageV3(BaseBirthdayMessage):
    def get_content(self, people):
        date = datetime.datetime.today()
        year = int(date.strftime("%Y"))
        if people.date_of_birth.year <= int(year - 49):
            return "Happy birthday, dear `" + str(
                people.first_name) + "`!(A greeting picture here)"
        else:
            return "Happy birthday, dear " + str(people.first_name) + "!"

