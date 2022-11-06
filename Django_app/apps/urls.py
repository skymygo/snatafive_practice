from django.urls import path
from apps.views import RollingPaperBoardListView
from apps.user_manage.social_account import social_naver_callback

app_name = 'checker_page'

urlpatterns = [
    path('rolling_paper/', RollingPaperBoardListView.as_view()),
    path('accounts/naver/login/callback/', social_naver_callback)
]
