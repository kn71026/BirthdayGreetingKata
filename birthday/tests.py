from django.test import TestCase
from django.test import client
from birthday.models import Birthday
from birthday.message import *


# Create your tests here.
class BirthdayTestCaseV1(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV1()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Sherry", last_name="Chen", gender="Female", date_of_birth="1993-08-08",
                                email="test2@test.com")

    def test_v1_simple_message_1(self):
        message_data = self.birthday_message.get()
        print(message_data.content.decode())
        self.assertEqual(message_data.content.decode(),
                         """Subject: Happy birthday!
Happy birthday, dear Robert!
Subject: Happy birthday!
Happy birthday, dear Cid!
Subject: Happy birthday!
Happy birthday, dear Sherry!
""")

    def test_v1_simple_message_2(self):
        message_data = self.birthday_message.get(8, 8)
        self.assertEqual(message_data.content.decode(),
                         """Subject: Happy birthday!
Happy birthday, dear Robert!
Subject: Happy birthday!
Happy birthday, dear Sherry!
""")


class BirthdayTestCaseV2(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV2()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Sherry", last_name="Chen", gender="Female", date_of_birth="1993-08-08",
                                email="test2@test.com")

    def test_v2_message_for_gender_1(self):
        message_data = self.birthday_message.get()
        self.assertEqual(message_data.content.decode(), """Subject: Happy birthday!
Happy birthday, dear Robert!
We offer special discount 20% off for the following items:
WhiteWine, iPhoneX
Subject: Happy birthday!
Happy birthday, dear Cid!
We offer special discount 20% off for the following items:
WhiteWine, iPhoneX
Subject: Happy birthday!
Happy birthday, dear Sherry!
We offer special discount 50% off for the following items:
Cosmetic, LV Handbags
""")

    def test_v2_message_for_gender_2(self):
        message_data = self.birthday_message.get(8, 8)
        self.assertEqual(message_data.content.decode(), """Subject: Happy birthday!
Happy birthday, dear Robert!
We offer special discount 20% off for the following items:
WhiteWine, iPhoneX
Subject: Happy birthday!
Happy birthday, dear Sherry!
We offer special discount 50% off for the following items:
Cosmetic, LV Handbags
""")


class BirthdayTestCaseV3(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV3()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Peter", last_name="Wang", gender="Male", date_of_birth="1950-12-22",
                                email="test3@test.com")

    def test_v3_message_for_gender_1(self):
        message_data = self.birthday_message.get()
        self.assertEqual(message_data.content.decode(), """Subject: Happy birthday!
Happy birthday, dear Robert!
Subject: Happy birthday!
Happy birthday, dear Cid!
Subject: Happy birthday!
Happy birthday, dear `Peter`!(A greeting picture here)
""")

    def test_v3_message_for_gender_2(self):
        message_data = self.birthday_message.get(12, 22)
        self.assertEqual(message_data.content.decode(), """Subject: Happy birthday!
Happy birthday, dear `Peter`!(A greeting picture here)
""")


class BirthdayTestCaseV4(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV4()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Sherry", last_name="Chen", gender="Female", date_of_birth="1993-08-08",
                                email="test3@test.com")

    def test_v4_simple_message_1(self):
        message_data = self.birthday_message.get()
        print(message_data.content.decode())
        self.assertEqual(message_data.content.decode(),
                         """Subject: Happy birthday!
Happy birthday, dear Yen, Robert!
Subject: Happy birthday!
Happy birthday, dear Change, Cid!
Subject: Happy birthday!
Happy birthday, dear Chen, Sherry!
""")

    def test_v4_simple_message_2(self):
        message_data = self.birthday_message.get(8, 8)
        self.assertEqual(message_data.content.decode(),
                         """Subject: Happy birthday!
Happy birthday, dear Yen, Robert!
Subject: Happy birthday!
Happy birthday, dear Chen, Sherry!
""")


class BirthdayTestCaseV5(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV5Json()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Sherry", last_name="Chen", gender="Female", date_of_birth="1993-08-08",
                                email="test3@test.com")

    def test_v5_simple_message_1(self):
        message_data = self.birthday_message.get()
        self.assertEqual(message_data.content.decode(),
                         """[{"title": "Subject: Happy birthday!", "content": "Happy birthday, dear Yen, Robert!"}, {"title": "Subject: Happy birthday!", "content": "Happy birthday, dear Change, Cid!"}, {"title": "Subject: Happy birthday!", "content": "Happy birthday, dear Chen, Sherry!"}]""")

    def test_v5_simple_message_2(self):
        message_data = self.birthday_message.get(8, 8)
        self.assertEqual(message_data.content.decode(),
                         """[{"title": "Subject: Happy birthday!", "content": "Happy birthday, dear Yen, Robert!"}, {"title": "Subject: Happy birthday!", "content": "Happy birthday, dear Chen, Sherry!"}]""")


class BirthdayTestCaseV5(TestCase):
    def setUp(self):
        self.birthday_message = BirthdayMessageV5Xml()
        Birthday.objects.create(first_name="Robert", last_name="Yen", gender="Male", date_of_birth="1975-08-08",
                                email="test@test.com")
        Birthday.objects.create(first_name="Cid", last_name="Change", gender="Male", date_of_birth="1990-10-10",
                                email="test2@test.com")
        Birthday.objects.create(first_name="Sherry", last_name="Chen", gender="Female", date_of_birth="1993-08-08",
                                email="test3@test.com")

    def test_v5_xml_simple_message_1(self):
        message_data = self.birthday_message.get()
        self.assertEqual(message_data.content.decode(),
                         """<root><list-item><title>Subject: Happy birthday!</title><content>Happy birthday, dear Robert!</content></list-item><list-item><title>Subject: Happy birthday!</title><content>Happy birthday, dear Cid!</content></list-item><list-item><title>Subject: Happy birthday!</title><content>Happy birthday, dear Sherry!</content></list-item></root>""")

    def test_v5_xml_simple_message_2(self):
        message_data = self.birthday_message.get(8, 8)
        self.assertEqual(message_data.content.decode(),
                         """<root><list-item><title>Subject: Happy birthday!</title><content>Happy birthday, dear Robert!</content></list-item><list-item><title>Subject: Happy birthday!</title><content>Happy birthday, dear Sherry!</content></list-item></root>""")
