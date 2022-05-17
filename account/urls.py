from django.urls import path
from django.conf.urls import include

from account.views import AccountView, AccountListView

urlpatterns = [
    path('<int:pk>', AccountView.as_view()),
    path('list', AccountListView.as_view()),
]
