from django.urls import path
from .views import home, add_review

urlpatterns = [
    path('', home, name='home'),
    path('add_review/', add_review, name='add_review'),
]
