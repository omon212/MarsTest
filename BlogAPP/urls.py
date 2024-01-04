from .views import NewsView
from django.urls import path

urlpatterns = [
    path('news/',NewsView.as_view(),name='news'),

]
