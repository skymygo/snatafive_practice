from django.contrib.auth.models import User
from test_plus.test import TestCase
from apps.models import User, Message

class MessageListViewTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        # User
        self.사용자A = User.objects.create()
        self.사용자B = User.objects.create()
        self.사용자C = User.objects.create()
        self.사용자D = User.objects.create()
        self.사용자E = User.objects.create()

    def test_사용자A의_링크를_조회한다(self):
        pass

    def test_사용자A의_링크로_사용자B가_접속하여_메시지를_보낸다(self):
        pass

    def test_사용자A에게_도착한_메시지를_확인한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자B로_확인한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자C로_확인한다(self):
        pass

    def test_사용자A에게_다량의_메시지를_보내고_확인한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자B로_수정한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자C로_수정한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_삭제한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자A가_답신한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자A가_지정일이_지난_시점으로_메시지를_확인한다(self):
        pass

    def test_사용자A가_회원_탈퇴한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자A가_회원_탈퇴한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자A가_회원_탈퇴한_뒤_사용자B로_메시지를_확인한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자B가_회원_탈퇴한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자B가_회원_탈퇴한_뒤_사용자A로_메시지를_확인한다(self):
        pass

    def test_사용자A에게_사용자B로_메시지를_보내고_사용자A가_회원_탈퇴_후_복구_요청한다(self):
        pass