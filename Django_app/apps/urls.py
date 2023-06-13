from django.urls import path
from apps.views import RollingPaperBoardListView, MessageListView
from apps.user_manage.social_account import social_naver_callback

app_name = 'checker_page'
from rest_framework import routers

router = routers.SimpleRouter()

router.register('rolling_paper', RollingPaperBoardListView)
router.register('message', MessageListView)

urlpatterns = [
                  path('accounts/naver/login/callback/', social_naver_callback)
              ] + router.urls

print(urlpatterns[0])
print(router.urls)
