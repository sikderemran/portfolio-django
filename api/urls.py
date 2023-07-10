from django.urls import path
from api.views.home import *
from api.views.about import *
from api.views.work import *
urlpatterns = [
    path('home', home.as_view()),
    path('about', about.as_view()),
    path('work', work.as_view()),
]
