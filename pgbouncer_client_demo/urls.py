from django.urls import path

from demo.views import BlockingTransationView

urlpatterns = [
    path('blocking-transaction/', BlockingTransationView.as_view()),
]
