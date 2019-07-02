from django.urls import path
from tracker.views import List

urlpatterns = [
    path('', List.as_view()),
]