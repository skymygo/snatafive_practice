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
            path='/rolling_paper/',
            data={
                'title': title,
                'opened_at': target_date,
                'board_image': 2
            }
        )

        return res

    def 롤링페이퍼_조회(self):
        res = self.client.get(
            path='/rolling_paper/'
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

        return data

    def test_사용자A가_롤링페이퍼보드를_만들고_조회한다(self):
        self.client.force_login(self.사용자A)

        created_rolling_paper = self.test_사용자A가_롤링페이퍼보드를_만든다()
        res = self.롤링페이퍼_조회()
        self.assertEqual(res.status_code, 200)

        get_rolling_paper = res.json()

        self.assertEqual(len(get_rolling_paper), 1)
        self.assertEqual(created_rolling_paper['id'], get_rolling_paper[0]['id'])

        return get_rolling_paper

    def test_사용자A가_롤링페이퍼보드를_6개_만든다(self):
        self.client.force_login(self.사용자A)

        for i in range(5):
            res = self.롤링페이퍼_생성('test_title')
            self.assertEqual(res.status_code, 201)

        res = self.롤링페이퍼_조회()
        self.assertEqual(res.status_code, 200)
        rolling_papers = res.json()
        self.assertEqual(len(rolling_papers), 5)

        res = self.롤링페이퍼_생성('test_title')
        self.assertEqual(res.status_code, 403)

        pass