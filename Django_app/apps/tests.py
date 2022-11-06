from django.contrib.auth.models import User
from django.test import TestCase
from apps.models import User, RollingPaperBoard, Message

import datetime

class MainScenarioTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        # User
        self.사용자A = User.objects.create(username='사용자A')
        self.사용자B = User.objects.create(username='사용자B')

    def 롤링페이퍼_생성(self, title, target_date=None):
        if target_date is None:
            target_date = datetime.datetime.now()
            target_date += datetime.timedelta(days=100)
        res = self.client.post(
            path='/rolling_paper',
            data={'title': title, }
        )

        return res

    def test_사용자A가_롤링페이퍼보드를_만든다(self):
        self.client.force_login(self.사용자A)

        test_title = '테스트 타이틀'

        res = self.롤링페이퍼_생성(test_title)
        self.assertEqual(res.status_code, 201)
        data = res.json()
        self.assertIsNotNone(data['id'])
        self.assertEqual(test_title, data['title'])

        rolling_paper = RollingPaperBoard.objects.get(pk=data["id"])
        self.assertEqual(data['id'], rolling_paper.id)
        self.assertEqual(data['title'], rolling_paper.title)

        return rolling_paper

    def test_사용자A가_롤링페이퍼보드를_조회한다(self):
        pass

    def test_사용자A가_롤링페이퍼보드를_6개_만든다(self):
        pass

    def test_사용자A가_롤링페이퍼보드를_4개_만들고_조회한다(self):
        pass