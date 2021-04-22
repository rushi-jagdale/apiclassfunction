from django.urls import path
from api import views

urlpatterns = [
    path('jsonapi',views.Jsoncbv.as_view()),
    path('jsonfbv',views.jsonfbv),
]
