from django.urls import path
from .views import news, feedback, workers_info

urlpatterns = [
    path('', news, name='news'),
    path('feedback/', feedback, name='feedback'),
    path('workers_info/', workers_info, name='workers-info'),
]

